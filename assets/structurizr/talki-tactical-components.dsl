workspace "Talki: diseño táctico" "Diseño objetivo del TP" {
  model {
    student = person "Estudiante"
    gemini = softwareSystem "Gemini Live"
    mail = softwareSystem "Correo"
    talki = softwareSystem "Talki" {
      bff = container "API Gateway / BFF" "Entrada autenticada" "HTTPS / JSON"
      web = container "Cliente web / móvil" "Recorrido de práctica" "Navegador / Flutter"
      bus = container "Broker de eventos" "Mensajes confirmados" "RabbitMQ"
      store = container "Material privado" "Archivos autorizados" "Almacenamiento de objetos"
      live = container "Live Coaching" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n1_api = component "LiveCoachController / LiveTokenResponse" "Interface: Valida preparación y cierre del ensayo" "Java / Spring Boot"
        n1_app = component "LiveCoachOrchestrator" "Application: Comprueba sesión/consentimiento y coordina credencial/cierre" "Java / Spring Boot"
        n1_rules = component "SessionModeStrategyFactory / estrategias" "Domain: Prepara instrucciones según modo y contexto" "Java / Spring Boot"
        n1_aiClient = component "AIProviderGatewayClient" "Infrastructure: Solicita credencial por API interna" "Java / Spring Boot"
        n1_sessionClient = component "SessionClosureClient / SessionAccessClient" "Infrastructure: Comprueba sesión y confirma evidencia de cierre" "Java / Spring Boot"
        n1_consentClient = component "ConsentVerificationClient" "Infrastructure: Consulta autorización vigente" "Java / Spring Boot"
      }
      analysis = container "Speech Analysis" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n2_consumer = component "SessionLiveFinalizedConsumer" "Infrastructure: Recibe el contrato AMQP y confirma tras commit" "Java / Spring Boot"
        n2_app = component "AnalyzeSpeechHandler" "Application: Coordina análisis y reintento sobre el mismo job" "Java / Spring Boot"
        n2_rules = component "AnalysisJob / FillerDetector / AcousticEvidenceAnalyzer / ContextualEvidenceAnalyzer" "Domain: Controla estado y analiza evidencia acústica/contextual" "Java / Spring Boot"
        n2_api = component "AnalysisJobController" "Interface: Consulta estado y solicita reintento interno" "Java / Spring Boot"
        n2_repo = component "AnalysisJobRepository / AnalysisResultOutbox" "Infrastructure: Conserva job y resultado durable" "Java / Spring Boot"
        n2_publisher = component "FillerAnalyzedPublisher" "Infrastructure: Despacha métricas confirmadas por RabbitMQ" "Java / Spring Boot"
      }
      db2 = container "Datos privados: Speech Analysis" "Esquema aislado" "PostgreSQL"
      scoring = container "Scoring & Feedback" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n3_consumer = component "FillerAnalyzedConsumer" "Infrastructure: Adapta el evento de análisis" "Java / Spring Boot"
        n3_api = component "ReportController" "Interface: Ofrece reporte, estado y solicitud de reintento" "Java / Spring Boot"
        n3_app = component "EvaluatePracticeHandler / ReportQueryHandler" "Application: Evalúa, registra y recupera resultados autorizados" "Java / Spring Boot"
        n3_rules = component "ScoreCalculator / ScoreResult / VoiceScore" "Domain: Calcula dimensiones respaldadas por evidencia" "Java / Spring Boot"
        n3_repo = component "ScoreResultRepository / ScoringOutbox" "Infrastructure: Mantiene unicidad por sesión y versiones" "Java / Spring Boot"
        n3_publisher = component "ScoringCompletedPublisher" "Infrastructure: Despacha evaluación confirmada" "Java / Spring Boot"
        n3_sessionClient = component "SessionAccessClient" "Infrastructure: Comprueba acceso y eliminación" "Java / Spring Boot"
        n3_analysisClient = component "AnalysisJobClient" "Infrastructure: Consulta estado y solicita reintento" "Java / Spring Boot"
      }
      db3 = container "Datos privados: Scoring & Feedback" "Esquema aislado" "PostgreSQL"
      sessions = container "Practice Session Management" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n4_api = component "SessionController" "Interface: Recibe preparación, consultas, material y cierre" "Java / Spring Boot"
        n4_app = component "SessionCommandService / SessionQueryService" "Application: Coordina escritura y consulta de prácticas" "Java / Spring Boot"
        n4_acl = component "SessionContextFacade" "Application: Adapta identidad externa al lenguaje de sesión" "Java / Spring Boot"
        n4_rules = component "Session / PracticeEvidence / Feedback / configuración / material" "Domain: Controla estados, evidencia y límites del ensayo" "Java / Spring Boot"
        n4_repo = component "SessionRepository / FeedbackRepository / MaterialRepository" "Infrastructure: Conserva evidencia y referencias de material privado" "Java / Spring Boot"
        n4_storage = component "PrivateMaterialStorageAdapter" "Infrastructure: Almacena o purga el archivo autorizado" "Java / Spring Boot"
        n4_messaging = component "UserRegisteredConsumer / SessionFinalizedPublisher" "Infrastructure: Actualiza proyección y despacha cierre confirmado" "Java / Spring Boot"
        n4_consentClient = component "ConsentVerificationClient" "Infrastructure: Verifica consentimiento de Identity" "Java / Spring Boot"
      }
      db4 = container "Datos privados: Practice Session Management" "Esquema aislado" "PostgreSQL"
      progress = container "Progress & Adaptation" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n5_api = component "ProgressController" "Interface: Expone dashboard, comparación y plan" "Java / Spring Boot"
        n5_app = component "RecordProgressHandler / UserProgressQueryService / BuildAdaptivePlanHandler" "Application: Actualiza historial, compara evidencia y prepara ejercicios" "Java / Spring Boot"
        n5_rules = component "UserProgress / SessionMetrics / AdaptivePlan" "Domain: Preserva compatibilidad y referencias de evidencia" "Java / Spring Boot"
        n5_repo = component "UserProgressRepository / SessionMetricsRepository / AdaptivePlanRepository" "Infrastructure: Conserva resultados, planes y ejercicios" "Java / Spring Boot"
        n5_consumer = component "ScoringCompletedConsumer" "Infrastructure: Recibe evaluación y delega actualización" "Java / Spring Boot"
      }
      db5 = container "Datos privados: Progress & Adaptation" "Esquema aislado" "PostgreSQL"
      sharing = container "Sharing & Retention" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n6_api = component "ShareController / DeletionController / ExportController" "Interface: Recibe solicitudes de privacidad y lectura compartida" "Java / Spring Boot"
        n6_app = component "CreateShareGrantHandler / ResolveSharedReportHandler / RevokeShareHandler / RequestDeletionHandler / CollectPurgeReceiptHandler / ExportReportHandler" "Application: Autoriza consultas y coordina permisos, exportación y purga" "Java / Spring Boot"
        n6_rules = component "ShareGrant / DeletionRequest / PurgeReceipt" "Domain: Controla vigencia, bloqueo y confirmaciones" "Java / Spring Boot"
        n6_repo = component "ShareGrantRepository / DeletionRequestRepository" "Infrastructure: Conserva hashes, solicitudes y confirmaciones" "Java / Spring Boot"
        n6_messaging = component "DeletionPublisher / PurgeReceiptConsumer" "Infrastructure: Solicita purga y recibe confirmaciones" "Java / Spring Boot"
        n6_clients = component "SessionAccessClient / AuthorizedReportClient" "Infrastructure: Bloquea sesión y recupera únicamente el reporte autorizado" "Java / Spring Boot"
      }
      db6 = container "Datos privados: Sharing & Retention" "Esquema aislado" "PostgreSQL"
      game = container "Gamification" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n7_api = component "GamificationController" "Interface: Expone racha y ranking voluntario" "Java / Spring Boot"
        n7_app = component "RecordGamificationHandler / GamificationQueryService" "Application: Registra contribuciones únicas y organiza consultas" "Java / Spring Boot"
        n7_rules = component "UserStreak / Achievement / PracticeContribution / AchievementRuleService" "Domain: Aplica validez, zona horaria y reglas versionadas" "Java / Spring Boot"
        n7_repo = component "UserStreakRepository / AchievementRepository / PracticeContributionRepository" "Infrastructure: Conserva progreso lúdico sin duplicar XP" "Java / Spring Boot"
        n7_messaging = component "ScoringCompletedConsumer / AchievementUnlockedPublisher" "Infrastructure: Recibe práctica evaluada y comunica logros" "Java / Spring Boot"
      }
      db7 = container "Datos privados: Gamification" "Esquema aislado" "PostgreSQL"
      identity = container "Identity & Access" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n8_api = component "AuthController / ProfileController / VoiceConsentController" "Interface: Recibe acceso, perfil, recuperación y consentimiento" "Java / Spring Boot"
        n8_app = component "AuthService / TokenSessionService / ConsentCommandService / PasswordRecoveryService" "Application: Coordina cuenta, tokens y autorizaciones" "Java / Spring Boot"
        n8_rules = component "AppUser / RefreshToken / VoiceConsent / PasswordResetRequest" "Domain: Mantiene identidad y vigencia/retiro/consumo" "Java / Spring Boot"
        n8_repo = component "AppUserRepository / RefreshTokenRepository / VoiceConsentRepository / PasswordResetRepository" "Infrastructure: Conserva registros privados de cuenta" "Java / Spring Boot"
        n8_security = component "PasswordEncoder / JwtTokenProvider" "Infrastructure: Protege contraseña y firma acceso" "Java / Spring Boot"
        n8_publisher = component "RabbitUserRegisteredPublisher / AccountNoticePublisher" "Infrastructure: Despacha avisos de cuenta sin secretos" "Java / Spring Boot"
      }
      db8 = container "Datos privados: Identity & Access" "Esquema aislado" "PostgreSQL"
      ai = container "AI Provider Gateway" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n9_api = component "AIProviderGatewayController" "Interface: Recibe contrato interno de credenciales" "Java / Spring Boot"
        n9_app = component "AIIntegrationApplicationService" "Application: Comprueba capacidad y selecciona proveedor" "Java / Spring Boot"
        n9_rules = component "AIProviderPort / LivePreparation / LiveCredential" "Domain: Define preparación independiente del proveedor" "Java / Spring Boot"
        n9_adapter = component "GeminiLiveClient" "Infrastructure: Emite credencial efímera por HTTPS" "Java / Spring Boot"
        n9_config = component "ProviderConfiguration" "Infrastructure: Obtiene secretos y capacidades de configuración protegida" "Java / Spring Boot"
      }
      notifications = container "Notifications" "Contexto y proceso de ejecución" "Java / Spring Boot" {
        n10_consumer = component "NotificationEventConsumer" "Infrastructure: Recibe eventos de evaluación, logro, cuenta y privacidad" "Java / Spring Boot"
        n10_api = component "NotificationPreferenceController" "Interface: Expone preferencias del destinatario" "Java / Spring Boot"
        n10_app = component "DispatchNotificationHandler / NotificationTemplateService / NotificationPreferenceService / NotificationRetryHandler" "Application: Prepara contenido, respeta preferencias y coordina reintento" "Java / Spring Boot"
        n10_rules = component "Notification / NotificationPreference / NotificationPushService" "Domain: Mantiene estado y contrato de entrega" "Java / Spring Boot"
        n10_repo = component "NotificationRepository / NotificationPreferenceRepository" "Infrastructure: Registra avisos únicos, intentos y preferencias" "Java / Spring Boot"
        n10_channels = component "WebSocketPushAdapter / EmailNotificationAdapter" "Infrastructure: Entrega aviso sin evidencia privada" "Java / Spring Boot"
      }
      db10 = container "Datos privados: Notifications" "Esquema aislado" "PostgreSQL"
    }
    n1_api -> n1_app "Delega caso de uso" "Java"
    n1_app -> n1_rules "Aplica reglas de dominio" "Java"
    n1_app -> n1_aiClient "Solicita credencial efímera" "Java"
    n1_app -> n1_sessionClient "Comprueba sesión y cierre" "Java"
    n1_app -> n1_consentClient "Verifica consentimiento" "Java"
    bff -> n1_api "Prepara ensayo y entrega cierre" "HTTPS / JSON"
    n1_aiClient -> ai "Solicita credencial efímera" "HTTPS / JSON"
    n1_sessionClient -> sessions "Verifica sesión y confirma cierre" "HTTPS / JSON"
    n1_consentClient -> identity "Verifica consentimiento vigente" "HTTPS / JSON"
    n2_api -> n2_app "Delega caso de uso" "Java"
    n2_consumer -> n2_app "Entrega evento validado" "Java"
    n2_app -> n2_rules "Aplica reglas de dominio" "Java"
    n2_app -> n2_repo "Lee y confirma datos del contexto" "Java"
    n2_app -> n2_publisher "Registra salida para despacho" "Java"
    bus -> n2_consumer "Entrega session.live.finalized" "AMQP"
    scoring -> n2_api "Consulta job o solicita reintento" "HTTPS / JSON"
    n2_repo -> db2 "Conserva job y outbox" "SQL / TLS"
    n2_publisher -> bus "Publica fillers.analyzed" "AMQP"
    n3_api -> n3_app "Delega caso de uso" "Java"
    n3_consumer -> n3_app "Entrega evento validado" "Java"
    n3_app -> n3_rules "Aplica reglas de dominio" "Java"
    n3_app -> n3_repo "Lee y confirma datos del contexto" "Java"
    n3_app -> n3_sessionClient "Comprueba sesión y cierre" "Java"
    n3_app -> n3_analysisClient "Consulta o reintenta análisis" "Java"
    n3_app -> n3_publisher "Registra salida para despacho" "Java"
    bus -> n3_consumer "Entrega fillers.analyzed" "AMQP"
    bff -> n3_api "Consulta reporte y estado" "HTTPS / JSON"
    n3_repo -> db3 "Conserva resultado y outbox" "SQL / TLS"
    n3_publisher -> bus "Publica scoring.completed" "AMQP"
    n3_sessionClient -> sessions "Verifica acceso a la sesión" "HTTPS / JSON"
    n3_analysisClient -> analysis "Consulta job o pide reintento" "HTTPS / JSON"
    n4_api -> n4_app "Delega caso de uso" "Java"
    n4_messaging -> n4_app "Entrega evento validado" "Java"
    n4_app -> n4_rules "Aplica reglas de dominio" "Java"
    n4_app -> n4_repo "Lee y confirma datos del contexto" "Java"
    n4_app -> n4_consentClient "Verifica consentimiento" "Java"
    n4_app -> n4_storage "Gestiona material autorizado" "Java"
    n4_app -> n4_acl "Adapta identidad externa" "Java"
    n4_app -> n4_messaging "Registra salida o confirmación" "Java"
    live -> n4_api "Comprueba sesión y confirma cierre" "HTTPS / JSON"
    scoring -> n4_api "Verifica acceso al reporte" "HTTPS / JSON"
    sharing -> n4_api "Confirma bloqueo y pertenencia" "HTTPS / JSON"
    bff -> n4_api "Crea o consulta práctica" "HTTPS / JSON"
    n4_repo -> db4 "Persiste sesión y outbox" "SQL / TLS"
    n4_storage -> store "Almacena o elimina material" "HTTPS"
    bus -> n4_messaging "Entrega user.registered y deletion.requested" "AMQP"
    n4_messaging -> bus "Publica cierre y confirmación de purga" "AMQP"
    n4_consentClient -> identity "Comprueba autorización actual" "HTTPS / JSON"
    n5_api -> n5_app "Delega caso de uso" "Java"
    n5_consumer -> n5_app "Entrega evento validado" "Java"
    n5_app -> n5_rules "Aplica reglas de dominio" "Java"
    n5_app -> n5_repo "Lee y confirma datos del contexto" "Java"
    bff -> n5_api "Consulta progreso o modifica plan" "HTTPS / JSON"
    bus -> n5_consumer "Entrega scoring.completed y deletion.requested" "AMQP"
    n5_consumer -> bus "Confirma purga local" "AMQP"
    n5_repo -> db5 "Lee y actualiza historial/planes" "SQL / TLS"
    n6_api -> n6_app "Delega caso de uso" "Java"
    n6_messaging -> n6_app "Entrega evento validado" "Java"
    n6_app -> n6_rules "Aplica reglas de dominio" "Java"
    n6_app -> n6_repo "Lee y confirma datos del contexto" "Java"
    n6_app -> n6_clients "Comprueba acceso y recupera reporte" "Java"
    n6_app -> n6_messaging "Registra salida o confirmación" "Java"
    bff -> n6_api "Comparte, revoca, exporta o elimina" "HTTPS / JSON"
    n6_repo -> db6 "Conserva permisos y solicitudes" "SQL / TLS"
    n6_messaging -> bus "Publica deletion.requested" "AMQP"
    bus -> n6_messaging "Entrega purge.completed" "AMQP"
    n6_clients -> sessions "Verifica propiedad y bloquea acceso" "HTTPS / JSON"
    n6_clients -> scoring "Consulta reporte autorizado" "HTTPS / JSON"
    n7_api -> n7_app "Delega caso de uso" "Java"
    n7_messaging -> n7_app "Entrega evento validado" "Java"
    n7_app -> n7_rules "Aplica reglas de dominio" "Java"
    n7_app -> n7_repo "Lee y confirma datos del contexto" "Java"
    n7_app -> n7_messaging "Registra salida o confirmación" "Java"
    bff -> n7_api "Consulta rachas y ranking" "HTTPS / JSON"
    bus -> n7_messaging "Entrega scoring.completed y deletion.requested" "AMQP"
    n7_messaging -> bus "Publica logro o confirma purga" "AMQP"
    n7_repo -> db7 "Persiste reconocimiento y contribuciones" "SQL / TLS"
    n8_api -> n8_app "Delega caso de uso" "Java"
    n8_app -> n8_rules "Aplica reglas de dominio" "Java"
    n8_app -> n8_repo "Lee y confirma datos del contexto" "Java"
    n8_app -> n8_security "Protege contraseña y acceso" "Java"
    n8_app -> n8_publisher "Registra salida para despacho" "Java"
    bff -> n8_api "Solicita acceso y perfil" "HTTPS / JSON"
    sessions -> n8_api "Verifica consentimiento vigente" "HTTPS / JSON"
    n8_repo -> db8 "Lee y conserva cuenta/tokens/consentimiento" "SQL / TLS"
    n8_publisher -> bus "Publica registro y aviso de cuenta" "AMQP"
    n9_api -> n9_app "Delega caso de uso" "Java"
    n9_app -> n9_rules "Aplica reglas de dominio" "Java"
    n9_app -> n9_adapter "Solicita credencial al proveedor" "Java"
    n9_app -> n9_config "Obtiene configuración protegida" "Java"
    live -> n9_api "Solicita preparación de credencial" "HTTPS / JSON"
    n9_adapter -> gemini "Obtiene credencial efímera" "HTTPS"
    n10_api -> n10_app "Delega caso de uso" "Java"
    n10_consumer -> n10_app "Entrega evento validado" "Java"
    n10_app -> n10_rules "Aplica reglas de dominio" "Java"
    n10_app -> n10_repo "Lee y confirma datos del contexto" "Java"
    n10_app -> n10_channels "Entrega aviso por canal" "Java"
    bus -> n10_consumer "Entrega eventos y deletion.requested" "AMQP"
    n10_consumer -> bus "Confirma purga de referencias de sesión" "AMQP"
    bff -> n10_api "Consulta/modifica preferencias" "HTTPS / JSON"
    n10_repo -> db10 "Conserva avisos y preferencias" "SQL / TLS"
    n10_channels -> web "Entrega aviso autenticado" "WSS"
    n10_channels -> mail "Envía mensaje transaccional" "HTTPS / SMTP-TLS"
  }
  views {
    component live "BC01" {
      include *
      autolayout tb
    }
    component analysis "BC02" {
      include *
      autolayout tb
    }
    component scoring "BC03" {
      include *
      autolayout tb
    }
    component sessions "BC04" {
      include *
      autolayout tb
    }
    component progress "BC05" {
      include *
      autolayout tb
    }
    component sharing "BC06" {
      include *
      autolayout tb
    }
    component game "BC07" {
      include *
      autolayout tb
    }
    component identity "BC08" {
      include *
      autolayout tb
    }
    component ai "BC09" {
      include *
      autolayout tb
    }
    component notifications "BC10" {
      include *
      autolayout tb
    }
    styles {
      element "Element" {
        color #ffffff
        background #1749b5
      }
    }
  }
}
