# Entorno y tecnología de Talki

**Qué significa entorno y tecnología en Talki.** La tecnología identifica con qué está construido cada componente. El entorno define dónde y con qué configuración se ejecuta ese código: equipo local, ambiente de pruebas o ambiente publicado. El entorno local, de integración o publicado utiliza el mismo stack, con su configuración correspondiente.

| Concepto | Ejemplo concreto en Talki | Qué documentamos |
| --- | --- | --- |
| Backend | Los ocho servicios Java con Spring Boot registran cuentas, gestionan sesiones y procesan resultados. | Lenguaje/framework, repositorio, versión, contrato y configuración. |
| Frontend | El cliente heredado Next.js/React presenta pantallas y utiliza un BFF para llamar a los servicios. | Framework real, navegación, consumo de APIs y gestión de sesión. |
| Mensajería | RabbitMQ comunica el cierre de práctica con análisis, puntuación, progreso y avisos. | Broker común, parámetros de conexión, eventos y recuperación. |
| Datos locales | H2 está configurada en memoria con create-drop. | Datos descartables para pruebas; no presentarlos como persistencia final de producción. |
| Proveedor de voz | Gemini Live requiere configuración privada para el ensayo de voz real. | Modelo configurado, credencial del servidor, token efímero y estados de error; nunca publicar la clave. |
| Entorno local | Los servicios y el broker se ejecutan en el equipo, con puertos de localhost. | Pasos reproducibles de arranque y fixtures de prueba. |
| Entorno de integración | Se ejecutan juntos los componentes necesarios para comprobar el recorrido. | Mismo ID de sesión, intercambios HTTP/eventos y resultados de aceptación. |
| Entorno publicado | Los productos están disponibles por HTTPS en recursos cloud. | URLs actuales, commit, variables externas y almacenamiento persistente, según el diseño de despliegue. |

**Decisión tecnológica del proyecto.** El Team Leader confirmó el 30/10/2026 conservar **Next.js 16.2.9, React 19.2.4 y TypeScript**, con **Tailwind CSS 4 y shadcn**, para el cliente web. Se reutilizan sus pantallas y BFF y se concentra el trabajo en integración, errores, pruebas y despliegue. Los ocho servicios se mantienen en Java 17/Spring Boot 3.2.5. La aplicación móvil Flutter continúa como ampliación propuesta; la vista responsive es parte del cliente web.

SB1-01-B documenta esta selección y comprueba su correspondencia con los archivos del cliente; SB1-06 integra el recorrido con los servicios. La migración a otro framework se retira del plan por decisión del equipo. H2 se utiliza en pruebas locales; la persistencia del ambiente publicado se configura y comprueba en SB1-07.

**Referencia del enunciado.** La sección Tecnología de la página 32 enumera Angular/Vue para Web Applications. Next.js/React es la decisión actual del equipo; esta edición del informe no modifica el documento del curso ni acredita autorización docente para esa diferencia. El [registro de tecnologías](../../assets/planning/sprint-1/technology-requirements.json) conserva el texto de origen y la decisión del proyecto.

Fuente: archivos del código reutilizado y página 32 de Trabajo Final_1ASI0728_202620.pdf, obtenido con Campus.
