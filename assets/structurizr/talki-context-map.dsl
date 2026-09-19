// Talki — Context Map (Strategic DDD, TB1)
// Referencia: README.md, sección 4.2.5.
//
// Cómo renderizar:
//   1) Editor online: https://structurizr.com/dsl  -> pegar este archivo -> "Render".
//   2) Structurizr Lite (local): https://docs.structurizr.com/lite -> copiar este
//      archivo como workspace.dsl en ui/workspace -> exportar PNG/SVG.
//   3) CLI: structurizr-cli export -workspace talki-context-map.dsl -format svg
//
// Exportar la vista "ContextMap" y guardarla como:
//   assets/images/context-mapping/context-map.png

workspace "Talki" "Context map — bounded contexts y patrones DDD (TB1)" {

    model {
        // Proveedor externo
        gemini = softwareSystem "Gemini Live API" "Proveedor externo de IA conversacional (C-01)" {
            tags "Sistema Externo"
        }

        group "Core Domain" {
            liveCoaching = softwareSystem "Live Coaching" "Interacción por voz en tiempo cercano al real: captura, transcripción incremental, señales de coaching y simulaciones." {
                tags "Bounded Context"
            }
            speechAnalysis = softwareSystem "Speech Analysis" "Procesa la transcripción consolidada y calcula métricas del discurso versionadas." {
                tags "Bounded Context"
            }
            scoring = softwareSystem "Scoring & Feedback" "Genera el Voice Coach Score, sugerencias priorizadas con evidencia y explicación por segmento." {
                tags "Bounded Context"
            }
        }

        group "Supporting Subdomains" {
            session = softwareSystem "Practice Session Management" "Ciclo de vida de la sesión: preparación, estados, material de contexto y veredicto de validez." {
                tags "Bounded Context"
            }
            progress = softwareSystem "Progress & Adaptation" "Historial, tendencias, comparación de sesiones y plan adaptativo." {
                tags "Bounded Context"
            }
            sharing = softwareSystem "Sharing & Retention" "Exportación, enlaces temporales revocables, revocación y retención de datos." {
                tags "Bounded Context"
            }
            gamification = softwareSystem "Gamification" "Rachas, niveles y logros para sostener el hábito de práctica." {
                tags "Bounded Context"
            }
        }

        group "Generic Subdomains" {
            identity = softwareSystem "Identity & Access" "Autenticación, cuentas, perfil y consentimiento verificable; Open Host Service de identidad." {
                tags "Bounded Context"
            }
            aiGateway = softwareSystem "AI Provider Gateway" "Contrato canónico de IA y aislamiento de proveedores (Anti-Corruption Layer)." {
                tags "Bounded Context"
            }
            notifications = softwareSystem "Notifications" "Notificaciones por correo a partir de hechos publicados por otros contextos." {
                tags "Bounded Context"
            }
        }

        // Identity & Access -> todos (OHS + PL, downstream Conformist)
        identity -> session "Valida identidad y consentimiento (OHS + PL, Conformist)"
        identity -> liveCoaching "Claims firmados verificados localmente (OHS + PL, Conformist)"
        identity -> scoring "Valida identidad y propiedad (OHS + PL, Conformist)"
        identity -> progress "Valida identidad y propiedad (OHS + PL, Conformist)"
        identity -> sharing "Valida identidad y propiedad (OHS + PL, Conformist)"
        identity -> gamification "Valida identidad (OHS + PL, Conformist)"
        identity -> notifications "Datos de contacto verificados (OHS + PL, Conformist)"

        // Practice Session Management
        session -> liveCoaching "Sesión preparada y veredicto de validez (Customer/Supplier + PL)"
        session -> speechAnalysis "Ciclo de vida y validez de la sesión (Customer/Supplier + PL)"
        session -> gamification "Hechos de práctica válida (Conformist)"

        // Núcleo
        liveCoaching -> speechAnalysis "Sesión Finalizada con transcripción consolidada (Customer/Supplier)"
        speechAnalysis -> scoring "Esquema versionado de métricas (Customer/Supplier + PL)"
        scoring -> progress "Reporte Disponible (Customer/Supplier)"
        scoring -> sharing "Reportes publicados (Customer/Supplier)"

        // Pasarela de IA
        liveCoaching -> aiGateway "Voz en vivo y simulación (Customer/Supplier)"
        speechAnalysis -> aiGateway "Análisis de discurso (Customer/Supplier)"
        aiGateway -> gemini "Contrato canónico traducido al proveedor (Anti-Corruption Layer)"

        // Progreso y gamificación
        progress -> gamification "Hechos de práctica válida (Conformist)"

        // Privacidad
        sharing -> speechAnalysis "Órdenes de eliminación propagadas (Customer/Supplier)"
        sharing -> progress "Órdenes de eliminación propagadas (Customer/Supplier)"
        sharing -> notifications "Acceso Revocado / Datos Purgados (Eventos publicados)"

        // Notificaciones
        scoring -> notifications "Reporte Disponible (Evento publicado)"
        identity -> notifications "Cuenta Registrada (Evento publicado)"
    }

    views {

        systemLandscape "ContextMap" "Context map de Talki (TB1)" {
            include *
            autoLayout
        }

        styles {
            element "Bounded Context" {
                background #438dd5
                color #ffffff
                shape RoundedBox
            }
            element "Sistema Externo" {
                background #999999
                color #ffffff
                shape Box
            }
        }

    }

}
