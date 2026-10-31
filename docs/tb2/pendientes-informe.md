# Pendientes del informe para TB2

Revisión del 30 de octubre de 2026. La prioridad es cerrar el informe acumulativo, desde la carátula hasta los anexos. El corte de contenido de TB2 es **7.4**; el Sprint 2, **7.2.2**, corresponde a TF1.

Fuentes: enunciado del curso obtenido con Campus, páginas 34–35, y comentarios generales del parcial `S07|TB1` (19/20). El [extracto de fuentes](../../assets/evidence/tb2/campus-scope-and-feedback.json) conserva el texto y el hash del enunciado. La numeración de UX sigue el informe actual: 6.4.3 mock-ups, 6.4.4 user flows y 6.5 prototipado.

**Las secciones tienen redacción, pero varias todavía contienen registros pendientes.** Una descripción o una plantilla preparada no reemplaza el acta, la prueba, la captura o el resultado que debe presentarse. Las casillas siguientes distinguen qué ya se documentó y qué impide cerrar el informe.

## Contenido documental disponible

- [x] **Capítulos I–V:** investigación, requisitos, diseño estratégico y diez bounded contexts con sus capas y diagramas. El profesor calificó diseño táctico y UX con 10/10; conservar lo aprobado.
- [x] **6.4.3, 6.4.4 y 6.5:** mock-ups, user flows y prototipo web/móvil descritos e ilustrados; alcance de la simulación identificado.
- [x] **7.1.1–7.1.4:** herramientas/versiones, repositorios, convenciones y configuración local redactados. El stack Next.js/React y Java/Spring Boot está elegido; el ambiente público sigue pendiente.
- [x] **7.2.1.3:** procedencia de los cinco repositorios reutilizados, rama, commit, fecha, autor y mensajes documentados. El [registro de origen](../../assets/evidence/tb2/development-commits.json) conserva la coautoría declarada; esos commits son de 202601.
- [x] **7.2.1.4:** resultado comprobado de 133 pruebas unitarias con JDK 17: cero fallos, errores u omisiones.
- [x] **7.2.1.5:** resultados reales de la prueba HTTP local, incluido el 500 al intentar finalizar una sesión DRAFT y el 503 esperado de Gemini sin clave.
- [x] **7.2.1.6:** métodos, rutas, parámetros, ejemplo de solicitud y ocho documentos OpenAPI locales disponibles.
- [x] **7.3.1:** diseño de validación, consentimiento, tareas, métricas y preguntas de cierre preparados.
- [x] **7.4:** introducción y guion del About Product redactados; publicación pendiente por indicación del equipo.
- [x] **Registro de versiones y bibliografía:** autoría editorial aclarada, versión 1.50 y referencias de los cinco repositorios de código añadidas.
- [x] **Conclusiones, recomendaciones y anexos:** avance TB2 incorporado, con límites de lo comprobado.

## Registros que faltan completar dentro del informe

- [x] **7.2.1.1 — Definición del Planning.** Fecha real 28/10, 20:00–21:00 por Google Meet y asistencia de cinco integrantes confirmados; objetivo, insumos, 36 SP residuales, 80 h de tareas, reparto de capacidad confirmado por el Team Leader, calendario, reglas de trabajo y Definition of Ready/Done definidos en el [plan detallado](sprint-1-plan.md).
- [x] **7.2.1.2 — Definición del Sprint Backlog.** Ocho PBIs y 24 tareas con responsables confirmados por el Team Leader, horas estimadas, dependencias, estado y aceptación; tablero actual con URL/capturas y hoja de ruta de las 37 US y seis TS publicados.
- [x] **Datos del acta.** Reunión del 28/10/2026, de 20:00 a 21:00 (Lima), por Google Meet, con los cinco integrantes presentes: confirmado por el Team Leader.
- [x] **Capacidad y responsables.** El Team Leader confirmó el 30/10/2026 las 20 h por integrante para el sprint 26/10–08/11 y los responsables definidos: 100 h de capacidad total, con 80 h estimadas de tareas, 10 h de coordinación/revisión y 10 h de reserva.
- [x] **7.2.1.1 — Calendario y responsabilidades.** Como equipo acordamos Sprint 1 del lunes 26/10 al domingo 08/11/2026, 20 h por integrante durante las dos semanas y división explícita de lo que realizará cada integrante. El planning del 28/10 está incluido en esa capacidad. La fecha institucional de Blackboard se conserva separada del cierre interno.
- [x] **Herramienta de tablero de la entrega.** GitHub Projects admitido según confirmación del Team Leader el 30/10/2026 y elegido por el equipo. Se conserva el tablero actual; no hace falta trasladarlo a otra herramienta. Quedan las actualizaciones de estados/evidencias conforme se ejecuten las tareas.
- [x] **7.2.1.3 — Trazabilidad documental.** Historial actual actualizado con repositorio, rama, SHA, fecha/hora, autor, mensaje y archivos. Matriz de ocho PBIs / 24 tareas con historias, coordinación futura, commits base y artefactos disponibles en el README.
- [ ] **7.2.1.3 — Evidencia de implementación.** Incorporar commit/PR de los cambios reales de software del incremento y sus pruebas. La consulta de la organización actual solo identifica el informe entre los repositorios accesibles; la base de aplicación permanece preservada con su procedencia 202601. La edición documental no se cuenta como desarrollo nuevo de servicios.
- [ ] **7.2.1.8 — Team Collaboration Insights.** Completar aportes y revisión de los cinco integrantes con commits/PR verificables y captura actual de colaboración. El PR de adaptación está enlazado; las revisiones sugeridas de otros integrantes no se presentan como realizadas.
- [ ] **Registro de versiones / Student Outcome.** Incorporar cada nueva modificación individual y las acciones que cada integrante realmente realizó en TB2; actualizar las conclusiones grupales acumulativas con esas acciones. La corrección de autoría histórica ya está hecha.

## Evidencia técnica que falta incorporar

- [x] **7.1.1 — Stack documentado y elegido.** Next.js/React/TypeScript con Tailwind/shadcn; servicios Java/Spring Boot. La selección fue confirmada por el Team Leader el 30/10/2026; la migración G-WEB se retiró del plan. La fuente académica original se conserva y no se presenta como autorización docente. Responsive web y móvil propuesto permanecen diferenciados.
- [ ] **7.1.4 y 7.2.1.7 — Despliegue.** Incorporar ambiente activo, configuración sin secretos, pasos ejecutados, commit desplegado, URLs funcionales y capturas actuales. El diagnóstico existente es 402 en el cliente y 404 en las 16 rutas históricas de backend consultadas; no demuestra una primera versión operativa.
- [ ] **7.2.1.4 — Testing.** Añadir pruebas ejecutadas de integración y aceptación BDD, con features/steps, comandos, commits y resultados. Las 133 unitarias ya están documentadas; no se convierten en evidencia de aceptación, rendimiento, privacidad o cobertura porcentual.
- [ ] **7.2.1.5 — Ejecución.** Incorporar capturas y explicación del recorrido integrado real, desde acceso hasta consulta del resultado. Registrar la transición válida de estados y la respuesta controlada al estado inválido. La comprobación actual no cubre voz real ni el cierre completo.
- [ ] **7.2.1.6 — Documentación de servicios.** Incorporar captura de Swagger UI y la URL del ambiente operativo, con ejemplos legibles de solicitud/respuesta y un error pertinente. Las especificaciones locales existentes se conservan como base.
- [x] **4.3.4 / capítulo V / 7.1–7.2 — Concordancia documentada.** Matriz de los diez contextos frente a los ocho servicios, con enlaces a archivos de commits fijados, alcance comprobado y diferencias. Sharing & Retention, gateway integrado, autorización, purga y reportes versionados están identificados en la [matriz de concordancia en 7.1.4](../../README.md#714-software-deployment-configuration); sus implementaciones pendientes no se marcan cerradas.

## Validación y referencias audiovisuales del informe

- [ ] **7.3.2 — Registro de entrevistas.** Completar entre tres y cinco participantes por segmento, con datos autorizados, fecha, dispositivo/versión, tareas realizadas, observaciones y síntesis individual. Actualmente hay seis registros vacíos preparados. Las entrevistas de needfinding de 2.2 no sustituyen estas sesiones.
- [ ] **7.3.3 — Evaluación heurística.** Completar hallazgos observados de usabilidad, arquitectura de información y diseño inclusivo: evidencia, frecuencia, severidad justificada, recomendación, responsable y estado. La matriz actual es un instrumento, no un resultado.
- [ ] **6.5 / 7.2.1.5 — Navegación.** Añadir captura, duración y enlace del recorrido grabado, identificando si corresponde al prototipo o al producto integrado.
- [ ] **7.3.2 — Video de validación.** Añadir captura, Stream e intervalos de las entrevistas cuando se publique. **Diferido por indicación del equipo.**
- [ ] **7.4 — About Product.** Añadir captura, duración, Stream/YouTube y referencia a la incrustación en la landing cuando exista. **Diferido por indicación del equipo; la introducción y el guion ya están redactados.**
- [ ] **Video About-the-Team / anexos.** Actualizar la descripción, el enlace y las evidencias de proceso/retrospectiva cuando se complemente la presentación individual ya enlazada.

Los registros y el análisis de validación también requieren que las sesiones se realicen: dejar pendiente el video no permite completar identidades, testimonios o hallazgos sin evidencia.

## Consolidación final del documento

- [x] **Conclusiones y recomendaciones del avance.** Síntesis actualizada con capacidad/plan confirmado, concordancia de contextos, pruebas y límites observados; no atribuye resultados a entrevistas o despliegues pendientes. Se revisará cuando cambien los resultados técnicos o de campo.
- [ ] **Bibliografía, figuras y anexos.** Revisar la correspondencia final de citas, referencias, atribución de figuras y enlaces; retirar de los anexos cualquier estado que se haya quedado desactualizado.
- [x] **Informe integrado en README.md.** Carátula, versiones, colaboración, índice, Student Outcome, capítulos I–VII, conclusiones, bibliografía y anexos conservados en el [README](../../README.md). Reproducción, concordancia y respuestas observadas están desarrolladas allí, además de sus fuentes de evidencia.
- **Word/PDF fuera del alcance actual**, por indicación del equipo: la prioridad y fuente de todo el contenido es README.md.

**Avance documental 1.46 en README.md:** correspondencia de arquitectura, procedimiento local, respuestas HTTP observadas, historial actual y conclusiones completados con fuentes verificables.

**Orden de trabajo restante:** ejecutar y evidenciar 7.1–7.2; incorporar aportes reales del equipo; realizar entrevistas y completar resultados de validación cuando se retomen. Actualizar el README cuando cambien esas evidencias. Las referencias audiovisuales acordadas pueden permanecer identificadas como pendientes durante esta revisión, sin marcar el entregable académico completo como terminado.
