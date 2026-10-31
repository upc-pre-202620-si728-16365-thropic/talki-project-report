# Definición de Sprint 1 para TB2

#### 7.2.1.1. Sprint Planning 1

Como equipo, acordamos organizar el Sprint 1 del **26/10/2026 al 08/11/2026**, con **20 h por integrante** y una distribución explícita de responsabilidades. La reunión de planning se realizó el **28 de octubre de 2026, de 20:00 a 21:00 (America/Lima), por Google Meet**, con los cinco integrantes presentes. El calendario inicia el lunes 26 y conserva el planning en su fecha real del miércoles 28. El objetivo, las tareas y sus criterios guían el trabajo; su cumplimiento se registra con evidencia, no por la sola asignación de un responsable.

**Sprint Goal.** Demostrar un recorrido integrado de acceso, preparación, práctica, cierre y consulta de feedback, aprovechando los ocho servicios existentes. Cada comportamiento presentado debe enlazar historia, tarea, commit, prueba y evidencia de ejecución. La meta es una primera versión demostrable; el cumplimiento completo de una User Story requiere todos sus criterios originales de 3.3.

| Campo | Definición y estado |
| --- | --- |
| Entrega / iteración | TB2 / Sprint 1 del periodo 202620. |
| Fecha de reunión | Miércoles 28/10/2026. |
| Modalidad y plataforma | Remota por Google Meet. |
| Hora de inicio y fin | 20:00–21:00, hora de Lima (UTC−05:00). |
| Duración | 60 minutos. |
| Organización del plan | Acuerdo del equipo Thropic; coordinación por bloque y responsables por tarea. |
| Integrantes asistentes | Alejandro Daniel Oroncoy Almeyda; Eduardo Gael Rivera Sosa; Manuel Ignacio Tumi Oliden; Werner Khalil Lang Nassi; Kevin Jorge Chi Cruzatt. |
| Asistencia efectiva a la reunión | Cinco de cinco integrantes presentes. |
| Inicio del sprint | Lunes 26/10/2026. |
| Cierre del sprint | Domingo 08/11/2026. |
| Duración del sprint | Dos semanas: 14 días calendario, con ambas fechas incluidas. |
| Fecha institucional de entrega | El enunciado sitúa TB2 en semana 12; confirmar fecha/hora publicada en Blackboard. El 08/11 es el cierre interno acordado del sprint. |
| Insumos | Capítulos I–VI; backlog de 3.5; ocho servicios reutilizados y cliente; 133 pruebas unitarias aprobadas; contratos y prueba HTTP local del 30/10. |
| Revisión previa | Feedback del parcial: 19/20, con diseño táctico/UX 10/10 y documentación/colaboración 9/10. |
| Mejora incorporada al plan | Aportes individuales verificables; documentación trazable; lámina del equipo y demostración de artefactos en herramientas. Son insumos del feedback; no se registra una retrospectiva adicional inexistente. |
| Estimación | 8 PBIs con 24 tareas: **36 SP residuales y 80 h de trabajo**. Las cifras son pronóstico inicial, no velocidad ni tiempo ejecutado; incluyen 6 h / 3 SP de validación diferida. |
| Capacidad acordada como equipo | 5 integrantes × 20 h = **100 h durante las dos semanas**: 80 h estimadas de tareas, 10 h de coordinación/revisión —incluido el planning— y 10 h de contingencia. Equivale a 10 h por integrante por semana. |
| Compromiso del equipo | Orientar SB1-01–SB1-07 al cierre del 08/11 conforme a sus criterios y accesos disponibles; registrar y resolver bloqueos, y comunicar cualquier ajuste de alcance. SB1-08 conserva responsables, pero su aplicación depende de las entrevistas diferidas. Ninguna asignación acredita una tarea terminada. |

**Base disponible y alcance pendiente.** La importación de código, los 133 resultados unitarios, los ocho documentos OpenAPI y los casos HTTP del 30/10 son insumos ya disponibles. No se estiman otra vez como si fueran desarrollo nuevo. El trabajo residual consiste en resolver diferencias, integrar, ejecutar aceptación, recuperar despliegue y documentar resultados. Las ampliaciones del producto se mantienen en la hoja de ruta completa, sin prometer su ejecución dentro de estas mismas 80 horas.

| Servicio o producto existente | Responsabilidad en la base | PBI que verifica o completa su integración |
| --- | --- | --- |
| identity-service | Registro, autenticación y segmento. | SB1-02; seguridad de acceso y BFF en SB1-06. |
| session-service | Sesiones, estados, consulta y feedback asociado. | SB1-02, SB1-03 y SB1-04. |
| live-coach-service | Modos, credencial efímera y evento de cierre de voz. | SB1-03. |
| filler-detection-service | Detección de muletillas desde el evento de cierre. | SB1-04. |
| scoring-service | Cálculo y publicación de puntuación. | SB1-04; proyecciones posteriores en SB1-05. |
| progress-service | Resumen del progreso a partir de evaluaciones. | SB1-05. |
| gamification-service | Rachas y logros según sesiones válidas. | SB1-05. |
| notification-service | Consumo de eventos de evaluación/logro y aviso disponible. | SB1-05. No se presume un canal de correo configurado. |
| Cliente web, landing y BFF | Pantallas, sesión del navegador y consumo de APIs. | SB1-02, SB1-03 y SB1-06 sobre Next.js/React. |
| RabbitMQ, persistencia y ambiente | Integración entre servicios y ejecución reproducible/desplegada. | SB1-01 y SB1-07. |

**Distribución de responsabilidades acordada como equipo.** Un coordinador por PBI organiza el cierre; las tareas de 7.2.1.2 indican quién hace cada parte. Las horas de apoyo se contabilizan a su responsable, no se suman de nuevo al coordinador.

Acordamos la siguiente división del trabajo. Las responsabilidades se expresan como acciones a realizar durante el sprint; las tareas de validación se mantienen asignadas y diferidas, como decidió el equipo.

| Integrante | Qué realizará | Tareas relacionadas |
| --- | --- | --- |
| Alejandro Daniel Oroncoy Almeyda | Coordinará el procedimiento de arranque, los estados y consentimiento de sesión, voz/token y cierre sin duplicados. Consolidará la trazabilidad técnica del informe. | SB1-01-A; SB1-03-A/B/C; SB1-07-C |
| Eduardo Gael Rivera Sosa | Documentará el stack Next.js/React; ajustará landing, conectará pantallas con APIs y comprobará el recorrido responsive. Mantendrá la responsabilidad de aplicar validación cuando se retomen las entrevistas. | SB1-01-B; SB1-06-A/B/C; SB1-08-A — diferida |
| Manuel Ignacio Tumi Oliden | Comprobará los contratos del pipeline, el feedback persistido y sus pruebas de integración/BDD. Verificará la actualización del progreso por eventos. | SB1-04-A/B/C; SB1-05-A |
| Werner Khalil Lang Nassi | Verificará acceso, logout y autorización por propietario; comprobará gamificación/notificaciones y la puerta de privacidad. Consolidará heurísticas cuando existan las sesiones de validación. | SB1-02-A/B; SB1-05-B; SB1-07-D; SB1-08-B — diferida |
| Kevin Jorge Chi Cruzatt | Documentará contratos/puertos; integrará errores de acceso y controles de práctica. Preparará los perfiles del ambiente y comprobará servicios y cliente publicados. | SB1-01-C; SB1-02-C; SB1-03-D; SB1-07-A/B |


| Integrante | Tareas asignadas en el plan | Trabajo | Coordinación / revisión | Reserva | Total confirmado |
| --- | --- | ---: | ---: | ---: | ---: |
| Alejandro Daniel Oroncoy Almeyda | SB1-01-A, SB1-03-A, SB1-03-B, SB1-03-C, SB1-07-C | 16 h | 2 h | 2 h | 20 h |
| Eduardo Gael Rivera Sosa | SB1-01-B, SB1-06-A, SB1-06-B, SB1-06-C, SB1-08-A | 16 h | 2 h | 2 h | 20 h |
| Manuel Ignacio Tumi Oliden | SB1-04-A, SB1-04-B, SB1-04-C, SB1-05-A | 16 h | 2 h | 2 h | 20 h |
| Werner Khalil Lang Nassi | SB1-02-A, SB1-02-B, SB1-05-B, SB1-07-D, SB1-08-B | 16 h | 2 h | 2 h | 20 h |
| Kevin Jorge Chi Cruzatt | SB1-01-C, SB1-02-C, SB1-03-D, SB1-07-A, SB1-07-B | 16 h | 2 h | 2 h | 20 h |
| **Total** | **24 tareas** | **80 h** | **10 h** | **10 h** | **100 h** |

Los SP de cada PBI usan la escala 1, 2, 3, 5 y 8 para estimar el **trabajo que queda** sobre la base reutilizada. Los SP originales de las User Stories y Technical Stories de 3.5 se conservan; no se suman a estos 36 puntos ni se convierten mediante una regla de horas por punto. La velocidad del equipo se medirá al cerrar trabajo realmente aceptado.

**Calendario del sprint y dependencias.** La secuencia organiza cierres, permitiendo iniciar antes las tareas cuyos insumos ya estén disponibles. Por ejemplo, el ambiente de SB1-07-A puede prepararse con SB1-01-C, aunque el despliegue integrado de SB1-07-B espere al cliente y al análisis.

| Fecha / periodo | Trabajo y coordinación previstos | Evidencia o salida requerida |
| --- | --- | --- |
| 26/10–27/10 | Inicio del periodo del sprint y preparación de insumos del backlog. | El periodo comienza el lunes 26; las tareas de esos días solo se registran como ejecutadas si existe evidencia. |
| 28/10, 20:00–21:00 | Planning por Google Meet con los cinco integrantes. | Reunión registrada; objetivo y organización del incremento. |
| 29/10–01/11 | Entorno, registro/acceso, contratos y landing: SB1-01, SB1-02 y SB1-06-A. | Base reproducible, stack elegido y acceso con fixtures; registrar el estado real de cada tarea. |
| 02/11–04/11 | Autorización, estados, voz, cierre y preparación del ambiente. | Sesión autorizada, correlación del evento y errores de negocio controlados. |
| 05/11–06/11 | Análisis/feedback, cliente integrado, progreso, logros y pruebas. | Reporte trazable; resultados de integración y aceptación con commit identificado. |
| 07/11–08/11 | Despliegue, matriz de evidencias, revisión y retrospectiva del sprint. | URLs/capturas actuales y balance real de terminado, bloqueado y pendiente al cierre del domingo 8. |
| Diferido, sin fecha de aplicación | Entrevistas y resultados de validación de SB1-08; videos. | Eduardo y Werner conservan sus responsabilidades; no se programan sesiones ni se atribuyen resultados mientras sigan diferidas. |

**Coordinación dentro de la capacidad.** Las 2 h por integrante incluyen 60 min del planning del 28/10, tres sincronizaciones previstas de 10 min, una review prevista de 20 min y una retrospectiva prevista de 10 min: 120 min en total. Las últimas actividades quedan por realizar. De las 100 h totales, el planning representa 5 h de equipo; descontando únicamente esa reunión confirmada quedan 95 h, sin deducir otros esfuerzos no medidos. Las 80 h de tareas incluyen 74 h técnicas/documentales y 6 h de validación asignada pero diferida; esas 6 h no se cuentan como ejecución ni como entrevista comprometida para el 08/11. Las 10 h de reserva absorben incidencias pequeñas.

**Definition of Ready.** Antes de iniciar una tarea deben existir su criterio de aceptación, responsable, dependencia resuelta, repositorio/commit de base e insumos de prueba. Si requiere credenciales, presupuesto cloud, acceso al proveedor o participantes, se registra el bloqueo concreto. Nunca se incluye un secreto en el tablero o en la captura.

**Definition of Done del incremento.** Cada PBI se acepta cuando: (1) el cambio está integrado y revisado mediante commit/PR; (2) sus pruebas unitarias pertinentes y la integración/aceptación correspondiente pasan; (3) contrato, estado de error y propiedad del recurso están comprobados; (4) la demostración usa datos identificados y muestra el alcance real; (5) el informe enlaza la evidencia del commit probado; y (6) el objetivo de despliegue usa el ambiente efectivo. Una historia completa solo se marca terminada si cumple todos los criterios de 3.3. Una captura de prototipo o de la base histórica no acredita esas condiciones.

**Criterios de aceptación de la review.** Se debe demostrar acceso, preparación, práctica corta, cierre y consulta del resultado con los dos perfiles académicos; repetir una finalización no debe duplicar la evaluación; una sesión inválida no debe inventar puntuación; un usuario no debe acceder a la sesión ajena. Los ocho servicios deben poder documentarse mediante OpenAPI en el ambiente mostrado, y las 133 pruebas base deben seguir aprobadas después de los cambios pertinentes. Se incorpora al menos un escenario BDD ejecutado con sus steps y un caso de error. El resultado observado de las tareas de validación se informa con su muestra real, sin prometer de antemano alcanzar QAS-USA-01.

**Decisiones operativas propuestas.** Limitar a una tarea de implementación en curso por integrante y dos revisiones simultáneas; actualizar diariamente el estado con evidencia; conservar la procedencia 202601; revisar autorización, consentimiento y privacidad antes de datos personales reales; y mantener los videos diferidos identificados como pendientes. Estas decisiones están definidas para ratificación, no se presentan como acta literal de acuerdos no aportados por el equipo.

#### 7.2.1.2. Sprint Backlog 1

El backlog sustituye las diez tareas genéricas iniciales por **ocho PBIs y 24 tareas**, todos definidos con responsable acordado como equipo, horas estimadas, dependencia y aceptación. El estado inicial es **Por hacer** para el trabajo residual; los activos existentes del 30/10 se conservan como base disponible y no convierten las historias completas en trabajo terminado.

| PBI | Incremento | Historias / contratos relacionados | Coordinación acordada | SP residuales | Trabajo | Dependencias para el cierre |
| --- | --- | --- | --- | ---: | ---: | --- |
| SB1-01 | Entorno reproducible, restricciones y trazabilidad | Transversal | Kevin | 2 | 8 h | Ninguna |
| SB1-02 | Identidad, acceso y aislamiento de sesiones | US05, US06, US20, US23, US28, US33 | Werner | 5 | 10 h | SB1-01 |
| SB1-03 | Práctica y ciclo de sesión con coaching | US09, US10, US12, US13, US14, US29, US34, US38, TS01, TS02 | Alejandro | 8 | 16 h | SB1-01, SB1-02 |
| SB1-04 | Análisis, puntuación y consulta de feedback | US15, US16, US20, US26, US37, TS03, TS04 | Manuel | 5 | 12 h | SB1-03 |
| SB1-05 | Progreso, logros y notificaciones por eventos | US21, US35, TS05 | Werner | 3 | 8 h | SB1-04 |
| SB1-06 | Landing y recorrido web coherentes con el incremento | US01, US02, US03, US04, US09, US15, US20, US29 | Eduardo | 5 | 10 h | SB1-01, SB1-02 |
| SB1-07 | Despliegue y evidencias de la primera versión | TS01, TS02, TS03, TS04 | Kevin | 5 | 10 h | SB1-01, SB1-02, SB1-03, SB1-04, SB1-05, SB1-06 |
| SB1-08 | Aplicación de validación y registro de hallazgos | US01, US09, US15, US20, US29, US33 | Eduardo | 3 | 6 h | SB1-06 |
| **Total** | **8 PBIs / 24 tareas** | **Cobertura mínima y trazable; criterios completos en 3.3** | **Equipo** | **36** | **80 h** | **Ver dependencias de tarea** |

**Base comprobada y trabajo restante.** Los estados siguientes describen el insumo real de cada PBI al 30/10. El estado `Todo` del tablero corresponde únicamente a las tareas residuales definidas; no significa que los servicios deban construirse desde cero.

| PBI / estado de base | Evidencia disponible | Trabajo residual estimado |
| --- | --- | --- |
| SB1-01 — Disponible | Ocho servicios compilados, 133 unitarias aprobadas y ocho OpenAPI locales capturados. | Cerrar runbook de clon limpio, decisión tecnológica y concordancia de contratos/despliegue. |
| SB1-02 — Parcial | Registro 201, login 200 y consulta/listado de una sesión fixture comprobados. | Verificar/logout, errores, expiración y autorización cruzada entre dos cuentas. |
| SB1-03 — Integración pendiente | Crear sesión 201, modos 200; finalizar DRAFT dio 500 y token sin clave dio 503 esperado. | Cerrar estados/consentimiento, voz configurada, correlación y cierre sin duplicados. |
| SB1-04 — Base disponible | 11 unitarias de detección de muletillas y 33 de scoring aprobadas; contratos de eventos presentes. | Comprobar recorrido asíncrono, consulta de feedback, errores, duplicados y aceptación BDD. |
| SB1-05 — Base disponible | 9 unitarias de progreso, 13 de gamificación y 7 de notificaciones; consultas iniciales de progreso/racha 200. | Demostrar actualización real por evento válido y que el duplicado no repite efectos. |
| SB1-06 — Cliente/prototipo disponibles | Compilación Next.js aprobada; galería y prototipo públicos dieron 200. | Integrar el recorrido real en Next.js/React y ajustar landing, errores y evidencias. |
| SB1-07 — Bloqueado por despliegue | En la comprobación del 30/10, frontend histórico 402 y 16 rutas Railway 404. | Acceso a recursos, perfiles/persistencia, publicación y verificación del ambiente efectivo. |
| SB1-08 — Protocolo listo | Guion de validación y registro de seis participantes preparado; sin sesiones o resultados acreditados. | Reclutar/aplicar a ambos segmentos y registrar observaciones y heurísticas reales. |

**SB1-01 — Entorno reproducible, restricciones y trazabilidad.** Servicios: Todos los servicios, Cliente web.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-01-A** Cerrar el runbook de arranque y configuración | Alejandro | 3 | Ninguna | Un clon limpio puede compilar con JDK 17, iniciar un único RabbitMQ y los ocho servicios; el runbook separa H2 local de persistencia pública y no expone secretos. | Por hacer |
| **SB1-01-B** Registrar decisiones de tecnología y alcance | Eduardo | 2 | Ninguna | Registrar Next.js/React/TypeScript, Tailwind y shadcn como stack elegido; relacionar versiones y BFF con los archivos del cliente. Conservar la fuente académica original y la decisión del equipo sin atribuir autorización docente no registrada. | Por hacer |
| **SB1-01-C** Versionar contrato y evidencia del entorno | Kevin | 3 | SB1-01-A | URLs/puertos, commit base, diagrama de despliegue ejecutable y ocho contratos OpenAPI coherentes; enlaces de las evidencias en el informe. | Por hacer |

**SB1-02 — Identidad, acceso y aislamiento de sesiones.** Servicios: identity-service, session-service, BFF del cliente.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-02-A** Verificar registro, login, segmento y logout | Werner | 4 | SB1-01-A | Registro nuevo 201, login válido 200, credenciales inválidas con respuesta controlada y logout invalida acceso del cliente; usar cuentas fixture y ocultar JWT. | Por hacer |
| **SB1-02-B** Implementar o comprobar autorización por propietario | Werner | 4 | SB1-02-A | Dos cuentas de prueba: el usuario B no puede leer, listar, finalizar o añadir feedback a la sesión de A. La identidad validada prevalece sobre userId enviado por el cliente. | Por hacer |
| **SB1-02-C** Integrar errores de acceso en el cliente | Kevin | 2 | SB1-02-A | Cliente conserva sesión en cookie httpOnly y presenta errores recuperables sin exponer token; prueba de expiración y retorno al login documentada. | Por hacer |

**SB1-03 — Práctica y ciclo de sesión con coaching.** Servicios: session-service, live-coach-service, Cliente web, Gemini Live.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-03-A** Cerrar máquina de estados y consentimiento | Alejandro | 4 | SB1-02-B | Ruta de inicio autorizada y transición DRAFT a RECORDING definidas; finalizar desde estado inválido devuelve error de negocio controlado, no 500. Registrar consentimiento antes de captura. | Por hacer |
| **SB1-03-B** Comprobar integración de voz y token efímero | Alejandro | 4 | SB1-03-A | Credencial permanente solo en servidor; permiso denegado, clave ausente y token vencido se comunican. Con configuración autorizada se prueba un ensayo corto sin publicar audio personal. | Por hacer |
| **SB1-03-C** Unificar finalización y evento de análisis | Alejandro | 4 | SB1-03-A, SB1-03-B | El ID persistido de sesión se conserva en coach y eventos; finalizar una vez produce una sola evaluación lógica. Repetir la petición no duplica resultados. | Por hacer |
| **SB1-03-D** Demostrar controles de práctica y errores | Kevin | 4 | SB1-03-B, SB1-03-C | Web muestra grabación, pausa/reanudación y cierre confirmado; permiso denegado y desconexión tienen recuperación o resultado parcial explícito. No declarar recuperación integral si no se verifica. | Por hacer |

**SB1-04 — Análisis, puntuación y consulta de feedback.** Servicios: filler-detection-service, scoring-service, session-service.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-04-A** Comprobar contratos del pipeline y duplicados | Manuel | 4 | SB1-03-C | Fixture recorre session.live.finalized, fillers.analyzed y scoring.completed con el mismo sessionId/userId; duplicado reconocido y fallo con estado visible. | Por hacer |
| **SB1-04-B** Persistir y consultar feedback mínimo trazable | Manuel | 4 | SB1-04-A | Reporte recuperable de la sesión del propietario contiene puntuación, muletillas, evidencia y límites. Estados pendiente/fallido no muestran una evaluación inventada; diferencias con TS04 versionado registradas. | Por hacer |
| **SB1-04-C** Ejecutar aceptación del recorrido de feedback | Manuel | 4 | SB1-04-B | Pruebas de integración y al menos un feature BDD ejecutable con steps verifican el caso feliz y un error; se adjuntan commit, comando y resultado. No convertir el conteo unitario en aceptación. | Por hacer |

**SB1-05 — Progreso, logros y notificaciones por eventos.** Servicios: progress-service, gamification-service, notification-service.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-05-A** Verificar proyección de progreso | Manuel | 4 | SB1-04-A | Scoring válido actualiza una sola vez el resumen del propietario; comparar el antes/después con el mismo fixture y conservar métricas/versiones disponibles sin inferir comparación avanzada. | Por hacer |
| **SB1-05-B** Verificar racha y aviso sin duplicados | Werner | 4 | SB1-05-A | Sesión válida activa la regla de racha/logro y el consumidor de notificaciones; reenvío del evento no duplica el efecto. Mostrar qué canal de aviso existe realmente; no afirmar envío de email no configurado. | Por hacer |

**SB1-06 — Landing y recorrido web coherentes con el incremento.** Servicios: Landing, Cliente web, BFF.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-06-A** Actualizar landing y estados vacíos | Eduardo | 4 | SB1-01-B | Beneficios y planes describen disponibilidad real; sin testimonios autorizados se muestra estado vacío. Contacto y videos identifican qué funciona y qué está pendiente. | Por hacer |
| **SB1-06-B** Integrar las pantallas con servicios reales | Eduardo | 4 | SB1-02-C, SB1-03-C, SB1-04-B | Acceso, preparación, práctica, reporte e historial consumen la base elegida; simulaciones y capturas de referencia están diferenciadas. Se reutiliza el cliente Next.js/React y se comprueba su integración; no se incluye una migración de framework. | Por hacer |
| **SB1-06-C** Comprobar usabilidad técnica web y responsive | Eduardo | 2 | SB1-06-B | Recorrido con teclado, foco, etiquetas, errores y vista móvil comprobado; responsive no se presenta como app nativa. Capturas corresponden al commit probado. | Por hacer |

**SB1-07 — Despliegue y evidencias de la primera versión.** Servicios: Ocho servicios backend, RabbitMQ, Persistencia, Cliente web.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-07-A** Preparar perfiles y recursos del ambiente | Kevin | 3 | SB1-01-C | Dominio/HTTPS, broker compartido, almacenamiento y variables externas documentados; H2 create-drop queda limitado al ambiente descartable. Acceso y presupuesto aprobados son dependencia externa. | Por hacer |
| **SB1-07-B** Publicar y comprobar servicios y cliente | Kevin | 4 | SB1-07-A, SB1-04-C, SB1-06-C | Las URLs del commit desplegado responden; OpenAPI y frontend funcionan contra el mismo ambiente. Una captura de despliegue histórico o un 200 de galería no cuenta como backend operativo. | Por hacer |
| **SB1-07-C** Cerrar matriz de trazabilidad técnica | Alejandro | 1 | SB1-07-B | Informe enlaza historia, tarea, servicio, commit, prueba y URL; los requisitos sin evidencia permanecen identificados. | Por hacer |
| **SB1-07-D** Verificar puerta de privacidad del despliegue | Werner | 2 | SB1-02-B, SB1-07-B | Aislamiento y consentimiento comprobados; hasta completar exportación/purga de TS06, el ambiente se limita a fixtures o acceso controlado y no admite un piloto con datos personales reales. | Por hacer |

**SB1-08 — Aplicación de validación y registro de hallazgos.** Servicios: Landing, Prototipo o cliente identificado.

| Tarea | Responsable acordado | Horas | Dependencias | Criterio de aceptación | Estado |
| --- | --- | ---: | --- | --- | --- |
| **SB1-08-A** Aplicar protocolo a ambos segmentos y registrar sesiones | Eduardo | 4 | SB1-06-C | Al menos tres participantes por segmento, consentimiento, fecha, dispositivo/versión y tareas; registrar éxito, tiempo, ayuda y observaciones. Si se usa prototipo, se declara simulación; reclutamiento es dependencia externa. | Por hacer |
| **SB1-08-B** Consolidar heurísticas y decisiones de mejora | Werner | 2 | SB1-08-A | Hallazgos reales de usabilidad, arquitectura de información y diseño inclusivo con severidad, evidencia y acción. Videos de validación y About Product siguen diferidos; no se inventan opiniones. | Por hacer |

**Reparto operativo por integrante para ejecutar el incremento.** Como equipo, acordamos los siguientes paquetes de trabajo para el sprint del 26/10 al 08/11. Cada integrante desarrollará sus tareas, comprobará los criterios de las tablas anteriores y actualizará su evidencia en este README. El reparto asigna trabajo futuro; las casillas se cerrarán cuando exista el resultado revisado.

Cada paquete conserva **16 h estimadas de tareas, 2 h de coordinación y 2 h de reserva**. En Eduardo hay 4 h de entrevistas diferidas y en Werner 2 h de heurísticas diferidas; el trabajo inmediato suma **74 h** y esas 6 h siguen asignadas sin fecha de aplicación. Videos e entrevistas permanecen pendientes.

**Alejandro Daniel Oroncoy Almeyda — Sesiones, voz y trazabilidad.**

Trabajará sobre [talki-session-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-session-services). Las referencias corresponden a la base de 202601; registrará el repositorio y la rama reales de sus cambios del sprint.

Empezará por SB1-01-A y la transición de inicio de sesión de SB1-03-A para desbloquear voz, análisis y cliente.

- [ ] **SB1-01-A — 3 h.** Verificará el arranque desde las instantáneas con JDK 17 y un solo RabbitMQ; corregirá en 7.1.4 los pasos o puertos que no se reproduzcan.
- [ ] **SB1-03-A — 4 h.** Resolverá DRAFT → RECORDING y el consentimiento antes de capturar voz; finalizar una sesión en estado inválido deberá devolver un error controlado, con prueba.
- [ ] **SB1-03-B — 4 h.** Comprobará el token efímero y un ensayo de voz con configuración autorizada; documentará permiso denegado, clave ausente y token vencido sin publicar claves ni JWT.
- [ ] **SB1-03-C — 4 h.** Mantendrá el mismo sessionId/userId al cerrar y publicar el evento; comprobará que repetir la finalización no produzca dos evaluaciones.
- [ ] **SB1-07-C — 1 h.** Consolidará en el README los enlaces reales de historia/tarea, commit probado, comando, resultado y URL del ambiente.

**Entregará:** Commit/PR del ciclo de sesión y voz; procedimiento de arranque comprobado; pruebas con resultados y matriz historia → tarea → servicio → commit → prueba → URL.

**Actualizará en el README:** 7.1.4; 7.2.1.3; 7.2.1.5; matriz técnica de cierre.

**Eduardo Gael Rivera Sosa — Cliente Next.js, landing y responsive.**

Trabajará sobre [talki-frontend](https://github.com/upc-pre-202601-si657-7940-thropic/talki-frontend). Las referencias corresponden a la base de 202601; registrará el repositorio y la rama reales de sus cambios del sprint.

Empezará por comprobar el stack del cliente y ajustar la landing; conectará las pantallas cuando estén disponibles los contratos de sesión y feedback.

- [ ] **SB1-01-B — 2 h.** Contrastará las versiones Next.js/React/TypeScript, Tailwind y shadcn con los archivos del cliente y mantendrá 7.1.1 alineado con el código real.
- [ ] **SB1-06-A — 4 h.** Ajustará beneficios, planes, contacto y estados vacíos de la landing a lo que funciona; identificará testimonios y videos todavía pendientes.
- [ ] **SB1-06-B — 4 h.** Conectará acceso, preparación, práctica, reporte e historial con las APIs a través del BFF; sustituirá simulaciones solo cuando exista el comportamiento real.
- [ ] **SB1-06-C — 2 h.** Comprobará navegación por teclado, foco, etiquetas, mensajes de error y vista móvil; entregará capturas de la versión probada.
- [ ] **SB1-08-A — 4 h.** **Diferido.** Conservará la responsabilidad de aplicar el protocolo a ambos segmentos; esta tarea seguirá diferida, sin entrevistas ni resultados ficticios.

**Entregará:** Commit/PR del frontend, resultado de compilación, capturas web/móvil y lista de pantallas conectadas y errores comprobados; registro de validación solo cuando se retomen entrevistas.

**Actualizará en el README:** 7.1.1; 7.2.1.5; evidencias de UI vinculadas a 6.3–6.5.

**Manuel Ignacio Tumi Oliden — Análisis, feedback, pruebas y progreso.**

Trabajará sobre [talki-analysis-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-analysis-services), [talki-engagement-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-engagement-services), [talki-session-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-session-services). Las referencias corresponden a la base de 202601; registrará el repositorio y la rama reales de sus cambios del sprint.

Empezará por revisar los contratos y preparar fixtures de eventos; ejecutará la cadena completa cuando Alejandro entregue el cierre correlacionado.

- [ ] **SB1-04-A — 4 h.** Comprobará session.live.finalized → fillers.analyzed → scoring.completed con el mismo sessionId/userId; verificará duplicados y fallo visible.
- [ ] **SB1-04-B — 4 h.** Verificará la persistencia y consulta del feedback del propietario, incluyendo score, evidencia, límites y estados pendiente/fallido; registrará lo que falte del contrato versionado.
- [ ] **SB1-04-C — 4 h.** Implementará y ejecutará integración y al menos un feature BDD con steps para caso feliz y error; guardará los resultados para 7.2.1.4.
- [ ] **SB1-05-A — 4 h.** Comparará progreso antes/después de una evaluación y comprobará que el evento repetido no vuelva a incrementar el resumen.

**Entregará:** Commit/PR del pipeline/feedback, pruebas de integración y BDD con feature/steps, comando y resultado; evidencia antes/después de la proyección de progreso.

**Actualizará en el README:** 7.2.1.4; 7.2.1.5; contratos de análisis y feedback de 7.2.1.6.

**Werner Khalil Lang Nassi — Acceso, gamificación, notificaciones y privacidad.**

Trabajará sobre [talki-user-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-user-services), [talki-session-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-session-services), [talki-engagement-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-engagement-services). Las referencias corresponden a la base de 202601; registrará el repositorio y la rama reales de sus cambios del sprint.

Empezará por SB1-02-A/B para desbloquear las verificaciones del propietario y el recorrido de sesión.

- [ ] **SB1-02-A — 4 h.** Comprobará registro, login, segmento, credenciales inválidas y logout; entregará resultados con cuentas fixture y tokens ocultos.
- [ ] **SB1-02-B — 4 h.** Probará con usuarios A/B que B no pueda leer, listar, finalizar o añadir feedback a la sesión de A; corregirá o documentará el control faltante.
- [ ] **SB1-05-B — 4 h.** Comprobará racha/logro y el consumidor de notificaciones después de una evaluación válida; repetirá el evento y mostrará el canal de aviso que exista realmente.
- [ ] **SB1-07-D — 2 h.** Verificará aislamiento y consentimiento del ambiente publicado; mientras falte G-PRIV, documentará y comprobará la limitación a fixtures/acceso controlado.
- [ ] **SB1-08-B — 2 h.** **Diferido.** Conservará la responsabilidad de consolidar hallazgos y heurísticas después de las entrevistas; esta tarea seguirá diferida.

**Entregará:** Commit/PR y pruebas con dos cuentas de fixture, resultados de racha/aviso sin duplicados y comprobación de la puerta de privacidad; heurísticas solo cuando existan sesiones reales.

**Actualizará en el README:** 7.2.1.4–7.2.1.6, controles de acceso/privacidad; heurísticas de 7.3.3 diferidas.

**Kevin Jorge Chi Cruzatt — Contratos, controles de práctica y despliegue.**

Trabajará sobre [talki-frontend](https://github.com/upc-pre-202601-si657-7940-thropic/talki-frontend), [talki-user-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-user-services), [talki-session-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-session-services), [talki-analysis-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-analysis-services), [talki-engagement-services](https://github.com/upc-pre-202601-si657-7940-thropic/talki-engagement-services). Las referencias corresponden a la base de 202601; registrará el repositorio y la rama reales de sus cambios del sprint.

Empezará por preparar contratos, recursos y perfiles; publicará el incremento cuando cliente, análisis y pruebas de integración estén disponibles.

- [ ] **SB1-01-C — 3 h.** Relacionará servicios, puertos, configuración y los ocho OpenAPI con el commit de base y el diagrama de despliegue; conservará los contratos revisados.
- [ ] **SB1-02-C — 2 h.** Comprobará en Next.js la cookie httpOnly, expiración de sesión, retorno al login y errores recuperables sin exponer el token.
- [ ] **SB1-03-D — 4 h.** Comprobará los controles de grabación, pausa/reanudación y cierre, además de permiso denegado y desconexión; registrará el resultado real.
- [ ] **SB1-07-A — 3 h.** Preparará perfiles, HTTPS, broker común, variables externas y almacenamiento persistente; documentará accesos o recursos que bloqueen la publicación.
- [ ] **SB1-07-B — 4 h.** Publicará el commit integrado y verificará cliente/APIs, Swagger y reinicio con datos fixture persistidos; incorporará URLs y capturas actuales en 7.2.1.7.

**Entregará:** Commit/PR de configuración e integración que corresponda, ocho contratos OpenAPI coherentes, capturas de Swagger, URLs funcionales, SHA desplegado y evidencia de persistencia.

**Actualizará en el README:** 7.1.4; 7.2.1.5–7.2.1.7.

**Entrega y revisión de cada paquete.** Cada integrante partirá de la versión integrada del informe en `main`, trabajará en una rama del repositorio de aplicación que corresponda y enlazará su commit/PR real. En el README incorporará: tarea/historia, repositorio y rama, SHA probado, comando y resultado de pruebas, capturas sin secretos y URL del ambiente cuando aplique. Registrará avance/bloqueos en GitHub Projects y actualizará su modificación en el registro de versiones y su acción en Student Outcome. Un compañero revisará la evidencia antes de marcar la tarea como terminada; las notas de participación se evaluarán al cierre.

**Orden para desbloquear al equipo.** Alejandro verificará el arranque y Werner comenzará acceso/propiedad; Eduardo podrá avanzar con stack y landing mientras Kevin prepara contratos/ambiente y Manuel prepara fixtures. Tras resolver estados y cierre de sesión, Manuel comprobará análisis/feedback; Eduardo conectará pantallas y Kevin comprobará controles. Con la proyección validada, Werner verificará gamificación/notificaciones. Finalmente, Kevin publicará y comprobará el ambiente, y Alejandro consolidará la trazabilidad. Si falta un insumo, se registrará la dependencia en la tarjeta; no se sustituirá el resultado con una captura histórica.

**Estados del tablero.** `Todo` equivale a Por hacer; `In Progress`, a En curso; `Done`, a Terminado con evidencia y revisión. Un bloqueo se registra en la tarjeta con causa, dependencia y responsable de resolución; no se oculta marcando la tarjeta como completada. El estado de aceptación de una US/TS se evalúa por sus criterios completos, separado del cierre de una tarea parcial.

**Tablero actual de revisión.** [Talki 202620 — TB2 — Sprint 1](https://github.com/orgs/upc-pre-202620-si728-16365-thropic/projects/1), vinculado al repositorio del informe. Sus tarjetas contienen las 24 tareas, dependencias y criterios; las columnas muestran coordinación, horas, SP y fase. La fecha del título corresponde al planning informado, no a la fecha de creación del tablero. Las capturas siguientes se tomaron el 30/10/2026 y muestran dos desplazamientos horizontales de la misma tabla.

![Tablero de Sprint 1 con PBIs, responsables y horas](../../assets/planning/sprint-1/github-project-items-20261030.jpg)

*Figura: Tablero real de revisión del periodo 202620. Todos los PBIs están pendientes de ejecución/aceptación; la captura muestra también G-WEB antes de su retiro posterior por decisión del equipo. La captura precede a la confirmación posterior de las asignaciones y las 20 h por integrante por el Team Leader el mismo 30/10/2026.*

![Columnas de horas, puntos y fase del tablero](../../assets/planning/sprint-1/github-project-20261030.jpg)

*Figura: Continuación horizontal del mismo tablero, con puntos y separación de paquetes condicionales. Las horas condicionales no forman parte del total de 80 h del Sprint 1. G-WEB aparece en esta captura anterior y fue retirado al confirmar Next.js/React; el snapshot del tablero registra el estado actualizado.*

**Herramienta de control del Sprint 1.** El equipo utilizará **GitHub Projects**, cuya admisión para esta entrega fue confirmada por el Team Leader el 30/10/2026. El tablero enlazado es la herramienta elegida para tareas, responsables, horas, estados y evidencias. La lista general de herramientas de la página 32 se conserva como fuente del enunciado; la confirmación del equipo cierra el pendiente de selección/aceptación, sin requerir traslado a Trello, Jira, YouTrack o Pivotal. El [CSV de tareas](../../assets/planning/sprint-1/sprint-backlog.csv) conserva una copia editable de las tareas del tablero.

**Paquetes que cambian la capacidad necesaria.** Se conserva Next.js/React y se retira G-WEB de la planificación activa; sus 48 h estimadas no se suman al sprint ni se cuentan como trabajo terminado. G-PRIV requiere **32 h adicionales estimadas** antes de un piloto con datos reales: el trabajo de entrega pasaría de 80 a 112 h, más coordinación/reserva, y requeriría replanificar capacidad o plazo. G-MEDIA sigue diferido.

| Paquete | Activación / objetivo | Responsable de coordinación | Estimación adicional | Condición de cierre |
| --- | --- | --- | ---: | --- |
| G-PRIV | Completar US27, US33 y TS06 antes de un piloto que procese datos personales reales. | Werner; apoyo de Manuel y Alejandro. | 32 h iniciales, alta incertidumbre. | Exportación, revocación, bloqueo, purga por contexto, confirmaciones, reintento, auditoría y pruebas. Mientras falte, limitar el ambiente a fixtures/acceso controlado. |
| G-MEDIA | Reactivar grabaciones y publicaciones cuando existan producto y testimonios reales. | Equipo. | 12 h orientativas de preparación/edición; reestimar según material. | Navegación, validación y About Product/Team según el enunciado. Los videos diferidos no se marcan publicados. |

**Hoja de ruta completa.** Se conservan las **37 User Stories y seis Technical Stories** de 3.5. La correspondencia siguiente señala la cobertura mínima del Sprint 1, el trabajo ampliado y las puertas antes de piloto. Las estimaciones originales de producto se mantienen. US21/US35 y otros elementos con capacidades heredadas pueden verificarse parcialmente ahora sin cambiar la prioridad de su implementación ampliada en el Product Backlog.

| ID | Historia / contrato | SP de producto (3.5) | PBI de Sprint 1 relacionado | Plan de cierre |
| --- | --- | ---: | --- | --- |
| US09 | Crear una sesión | 3 | SB1-03, SB1-06, SB1-08 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US12 | Iniciar grabación y transcripción | 8 | SB1-03 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US14 | Finalizar y guardar | 3 | SB1-03 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US15 | Recibir feedback general | 8 | SB1-04, SB1-06, SB1-08 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US01 | Visualizar beneficios | 2 | SB1-06, SB1-08 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US02 | Ver planes y precios | 2 | SB1-06 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US03 | Ver testimonios | 1 | SB1-06 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US04 | Enviar una consulta | 2 | SB1-06 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US38 | Recibir coaching en tiempo cercano al real | 8 | SB1-03 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US16 | Analizar muletillas | 5 | SB1-04 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US19 | Recibir sugerencias por sección | 5 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US26 | Recibir recomendaciones por segmento | 5 | SB1-04 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US37 | Consultar estado y reintentar análisis | 5 | SB1-04 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US20 | Consultar historial | 3 | SB1-02, SB1-04, SB1-06, SB1-08 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US29 | Verificar micrófono y consentimiento | 5 | SB1-03, SB1-06, SB1-08 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US34 | Recuperar una sesión interrumpida | 8 | SB1-03 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US33 | Revocar consentimiento y eliminar datos | 8 | SB1-02, SB1-08 | Puerta obligatoria antes de piloto con datos reales. Control de acceso/consentimiento revisado en Sprint 1; exportación y purga distribuidas requieren el paquete G-PRIV antes de usuarios reales. |
| US10 | Seleccionar tipo de sesión | 3 | SB1-03 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US23 | Seleccionar segmento académico | 2 | SB1-02 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US05 | Registrar una cuenta | 5 | SB1-02 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US06 | Iniciar sesión | 5 | SB1-02 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US28 | Cerrar sesión | 1 | SB1-02 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US13 | Pausar y reanudar | 3 | SB1-03 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US08 | Editar perfil | 3 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US11 | Configurar duración objetivo | 2 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US24 | Establecer metas | 3 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US25 | Seleccionar áreas de enfoque | 3 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US30 | Cargar material de contexto | 8 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US31 | Simular entrevista o sustentación | 8 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US17 | Analizar palabras clave | 5 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US18 | Mejorar el léxico | 5 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US21 | Ver progreso | 5 | SB1-05 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US22 | Comparar sesiones | 5 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US36 | Recibir un plan adaptativo | 8 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| US27 | Exportar transcripción y feedback | 3 | No comprometido en este incremento | Puerta obligatoria antes de piloto con datos reales. Control de acceso/consentimiento revisado en Sprint 1; exportación y purga distribuidas requieren el paquete G-PRIV antes de usuarios reales. |
| US35 | Mantener rachas y logros | 5 | SB1-05 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| US07 | Recuperar contraseña | 3 | No comprometido en este incremento | Siguiente incremento / Sprint 2. Capacidad ampliada del producto; conservar criterios originales y refinar antes de comprometer. |
| TS01 | API de sesiones | 3 | SB1-03, SB1-07 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| TS02 | Contrato de coaching en vivo | 8 | SB1-03, SB1-07 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| TS03 | Pipeline de análisis idempotente | 8 | SB1-04, SB1-07 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| TS04 | Consulta de reportes versionados | 5 | SB1-04, SB1-07 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| TS05 | API de progreso | 5 | SB1-05 | Sprint 1: incremento mínimo. Cobertura de la base y de los criterios incluidos en los PBIs; aceptación completa de la US/TS solo con todos sus criterios originales comprobados. |
| TS06 | API de exportación y eliminación | 8 | No comprometido en este incremento | Puerta obligatoria antes de piloto con datos reales. Control de acceso/consentimiento revisado en Sprint 1; exportación y purga distribuidas requieren el paquete G-PRIV antes de usuarios reales. |

La fuente estructurada es [plan.json](../../assets/planning/sprint-1/plan.json); el [CSV de hoja de ruta](../../assets/planning/sprint-1/product-roadmap.csv) facilita contrastar la cobertura de cada ID. El [snapshot del tablero](../../assets/planning/sprint-1/board-snapshot.json) preserva tarjetas y campos al publicarlo. El tablero histórico de 202601 se utiliza únicamente como antecedente.
