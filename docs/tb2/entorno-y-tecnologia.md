# Entorno y tecnología de Talki

**Qué significa entorno y tecnología en Talki.** La tecnología identifica con qué está construido cada componente. El entorno define dónde y con qué configuración se ejecuta ese código: equipo local, ambiente de pruebas o ambiente publicado. Cambiar una URL o una variable de entorno no convierte Next.js en Angular ni Vue.

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

**Diferencia con el enunciado.** La página 32 admite Java/Spring Boot para servicios: esa parte de la base coincide. Para la aplicación web enumera Angular o Vue y bibliotecas de componentes de Material Design: Angular Material/PrimeNG o PrimeVue/Vuetify, según el framework. La base heredada usa Next.js/React con Tailwind/shadcn, por lo que la conformidad de la aplicación web debe resolverse mediante una adecuación real o autorización expresa del docente. **Nest Framework**, permitido como alternativa de backend, y **Next.js**, usado por el cliente heredado, son tecnologías distintas. El diseño responsive del navegador tampoco acredita una aplicación móvil nativa.

El plan trata esta diferencia como una decisión de alcance en SB1-01-B y, si se requiere adecuación, como el paquete adicional G-WEB. No se rehacen automáticamente los ocho servicios Java por cambiar el framework de las pantallas. Por separado, H2 sirve para las pruebas locales; la persistencia del ambiente publicado se configura y comprueba en SB1-07.

Fuente: archivos del código reutilizado y página 32 de Trabajo Final_1ASI0728_202620.pdf, obtenido con Campus.
