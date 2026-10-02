# Complementos UX de Talki

Artefacto auxiliar de diseño del capítulo VI. El prototipo principal es el [cliente web de Talki](https://talki-frontend.vercel.app), que incluye acceso, dashboard, Coach, sesiones, grabación y feedback.

En escritorio, esas seis vistas del auxiliar presentan sus capturas originales y un enlace al cliente web. Las capturas son estáticas. Los complementos interactivos cubren las pantallas y estados adicionales; la vista móvil es una propuesta de adaptación. Los colores de `tokens.css` proceden de `src/app/globals.css` del frontend Talki, versión `d63e889a216d093a86bf24a2a328c18d0e610618`. El tema claro usa naranja `#F97316`, fondo `#F7F8FC` y texto `#0F172A`. El archivo conserva también los valores del tema oscuro. Los controles y tablas utilizan esos tokens.

Abre `index.html` en un navegador o sirve la raíz del repositorio con:

```sh
python3 -m http.server 8000
```

Visita `http://localhost:8000/assets/ux/prototype/`. El HTML en GitHub muestra código, no ejecuta la aplicación. No requiere instalación de paquetes o conexión a servicios externos.

- Vista web: ventana de escritorio; mock-ups exportados a 1440 px.
- Vista móvil: ventana de 390 px; navegación inferior a ≤ 700 px.
- Wireframe: `index.html?view=wireframe`.
- Pantalla directa: hash `#setup`, `#microphone`, `#live`, `#report`, `#privacy`, etc.
- Recargar la página restaura los datos de ejemplo.

La vista inicial es privacidad. Para preparar una práctica, abre `#setup` y pulsa **Explorar material contextual**; en móvil se muestra directamente la propuesta de configuración. En audio, pulsa **Simular prueba correcta** y marca el consentimiento para habilitar **Iniciar práctica**. Puedes pausar, reanudar, simular desconexión y confirmar el cierre. En análisis, elige reporte disponible, fallo o evidencia insuficiente. En privacidad, crea un acceso de ejemplo, consulta como tutor, revoca y verifica que ya no se muestre el reporte. La eliminación requiere confirmación y permanece como purga pendiente.

Los datos, nombres de personas, transcripción, puntuaciones, gráfico y cronómetro son ficticios. No hay autenticación real, IA, micrófono, backend, correo, cobro o purga física. El archivo de material solo se valida por nombre/tamaño, no se lee ni envía. El estado del recorrido vive en memoria; no se guardan datos personales. Las rutas directas ayudan a revisar pantallas y no representan autorización de un producto en producción.

Los wireframes describen las estructuras de pantallas y navegación en escala de grises. Las seis capturas web existentes no se vuelven a generar como mock-ups. Las capturas se encuentran en `../wireframes/` y `../mockups/`. Los flujos editables están en `../../diagrams/ux/`.
