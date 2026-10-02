# Prototipo UX de Talki

Artefacto de diseño del capítulo VI para el segundo hito de TB1, semana 7.

Abre `index.html` en un navegador o sirve la raíz del repositorio con:

```sh
python3 -m http.server 8000
```

Visita `http://localhost:8000/assets/ux/prototype/`. El HTML en GitHub muestra código, no ejecuta la aplicación. No requiere instalación de paquetes o conexión a servicios externos.

- Vista web: ventana de escritorio; mock-ups exportados a 1440 px.
- Vista móvil: ventana de 390 px; navegación inferior a ≤ 700 px.
- Wireframe: `index.html?view=wireframe`.
- Pantalla directa: hash `#setup`, `#microphone`, `#live`, `#report`, `#privacy`, etc.
- Reiniciar recorrido: botón superior; restaura datos de ejemplo.

Explora el flujo de registro, perfil y práctica. En audio, pulsa **Simular prueba correcta** y marca el consentimiento para habilitar **Iniciar práctica**. Puedes pausar, reanudar, simular desconexión y confirmar el cierre. En análisis, elige reporte disponible, fallo o evidencia insuficiente. En privacidad, crea un acceso de ejemplo, consulta como tutor, revoca y verifica que ya no se muestre el reporte. La eliminación requiere confirmación y permanece como purga pendiente.

Los datos, nombres de personas, transcripción, puntuaciones, gráfico y cronómetro son ficticios. No hay autenticación real, IA, micrófono, backend, correo, cobro o purga física. El archivo de material solo se valida por nombre/tamaño, no se lee ni envía. El estado del recorrido vive en memoria; no se guardan datos personales. Las rutas directas ayudan a revisar pantallas y no representan autorización de un producto en producción.

Los wireframes usan las mismas pantallas y navegación con estilo de estructura en escala de grises. Las capturas se encuentran en `../wireframes/` y `../mockups/`. Los flujos editables están en `../../diagrams/ux/`.
