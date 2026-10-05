# Prototipo UX de Talki

Recorrido de diseño para web y móvil del capítulo VI, con datos de ejemplo. Las interacciones son simuladas y el estado vive en memoria; no solicita micrófono ni conecta servicios, IA o almacenamiento. El archivo opcional solo se valida por nombre/tamaño y no se lee ni envía.

Sirve la raíz del repositorio con `python3 -m http.server 8000` y visita `http://localhost:8000/assets/ux/prototype/`. El enlace HTML en GitHub muestra código, por lo que se debe abrir localmente o mediante un servidor estático.

- Vista predeterminada: interacción web; a 390 px se adapta a móvil.
- `?view=wireframe`: estructura en escala de grises.
- `?reference=1`: conserva las seis capturas web del cliente como referencia visual estática.
- Hashes: `#setup`, `#microphone`, `#live`, `#processing`, `#report`, `#history`, `#compare`, `#plan`, `#privacy`, `#shared`, `#terms`.

En preparación, completa título/meta, selecciona modo y continúa. Comprueba el audio simulado y acepta el consentimiento para iniciar. Pausa o simula desconexión, reanuda y confirma el cierre. En análisis, explora fallo/reintento o un reporte parcial. En historial, filtra y compara; las versiones incompatibles se bloquean. El plan permite marcar un ejercicio y volver a practicar. En privacidad, comparte, consulta como tutor, revoca y confirma eliminación; se distingue el bloqueo de acceso de la purga pendiente. Recargar reinicia los datos.

Los términos propuestos se acceden desde los footers públicos y de aplicación. El recorrido principal se presenta en español. El diseño bilingüe de en_US/es_419 se ilustra aparte en el informe; la integración del catálogo completo de traducciones y servicios está pendiente. La captura y publicación de las demostraciones por aplicación en Microsoft Stream también están pendientes.

El naranja #F97316 mantiene la marca; sus controles usan texto #0F172A. Los enlaces usan #9A3412 y el foco permanece visible. Las capturas originales se preservan como referencias del cliente; las pantallas de propuesta reflejan los ajustes de accesibilidad.
