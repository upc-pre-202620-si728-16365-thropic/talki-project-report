#!/usr/bin/env bash
# Enciende, apaga o consulta el ambiente TB2 de Talki en Railway (proyecto talki-tb2).
# Requisitos: railway CLI con sesión iniciada en la cuenta dueña del proyecto y gh CLI.
#   scripts/talki-cloud.sh status          # estado y health de cada servicio
#   scripts/talki-cloud.sh up [servicio]   # sube el código fijado en REFS y despliega (3-6 min)
#   scripts/talki-cloud.sh down [servicio] # retira el despliegue: deja de consumir CPU/RAM
# Postgres y RabbitMQ conservan sus datos. Variables y dominios no cambian.
set -euo pipefail

PROJECT_ID="6069dedc-f0de-4dcf-bea4-eb052b3c16e7"
ENVIRONMENT="production"
ORG="upc-pre-202620-si728-16365-thropic"

# servicio | repositorio | rama o commit | carpeta
REFS="identity-service|talki-user-services|develop|identity-service
notification-service|talki-user-services|develop|notification-service
session-service|talki-session-services|feat/sb1-03-session-lifecycle|session-service
live-coach-service|talki-session-services|feat/sb1-03-session-lifecycle|live-coach-service
filler-detection-service|talki-analysis-services|main|filler-detection-service
scoring-service|talki-analysis-services|main|scoring-service
progress-service|talki-engagement-services|main|progress-service
gamification-service|talki-engagement-services|main|gamification-service"

INFRA="Postgres rabbitmq"
action="${1:-status}"; only="${2:-}"
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
cd "$work"
railway link -p "$PROJECT_ID" -e "$ENVIRONMENT" >/dev/null

selected() { [ -z "$only" ] || [ "$only" = "$1" ]; }

health() {
  local domain
  domain="$(railway domain -s "$1" 2>/dev/null | grep -o 'https://[^ ]*' | head -1 || true)"
  [ -n "$domain" ] && curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$domain/actuator/health" || echo "-"
}

case "$action" in
  status)
    for s in $INFRA; do printf '%-26s %s\n' "$s" "$(railway service status -s "$s" 2>&1 | tail -1)"; done
    while IFS='|' read -r svc _ _ _; do
      printf '%-26s %-26s health=%s\n' "$svc" "$(railway service status -s "$svc" 2>&1 | tail -1)" "$(health "$svc")"
    done <<< "$REFS"
    ;;
  up)
    while IFS='|' read -r svc repo ref dir; do
      selected "$svc" || continue
      [ -d "$repo" ] || gh repo clone "$ORG/$repo" "$repo" -- -q
      git -C "$repo" fetch -q origin "$ref" && git -C "$repo" checkout -q FETCH_HEAD
      sha="$(git -C "$repo" rev-parse --short HEAD)"
      echo "== $svc <- $repo@$ref ($sha)"
      railway up "$repo/$dir" --path-as-root -p "$PROJECT_ID" -e "$ENVIRONMENT" -s "$svc" -d -m "talki-cloud up $repo@$ref $sha" | tail -1
    done <<< "$REFS"
    echo "Construyendo. Revisa con: $0 status"
    ;;
  down)
    while IFS='|' read -r svc _ _ _; do
      selected "$svc" || continue
      echo "== $svc"; railway down -s "$svc" -e "$ENVIRONMENT" -y || true
    done <<< "$REFS"
    ;;
  *) echo "Uso: $0 status|up|down [servicio]"; exit 1 ;;
esac
