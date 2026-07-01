# 🤖 Proyecto Juan: Guía Completa de Capacidades

El proyecto **Juan** (anteriormente Jarvis) es un asistente virtual híbrido avanzado. Está compuesto por tres grandes módulos que trabajan juntos en tiempo real:
1. **Cerebro (Java Spring Boot)**: Procesa el lenguaje natural, guarda el historial y gestiona la memoria.
2. **Sistema Nervioso (Python Daemon)**: Controla el micrófono, los altavoces, las ventanas de Windows y el navegador web.
3. **Interfaz (Dashboard Web HTML/JS)**: Ofrece un panel de control visual para monitoreo y control manual.

A continuación, se detalla **paso a paso todo lo que puede hacer este proyecto actualmente:**

---

## 🗣️ 1. Interacción por Voz Súper Natural
- **Escucha Continua (Wake Word)**: Juan escucha todo el tiempo en segundo plano, pero solo despierta y presta atención a tu comando si inicias la frase diciendo la palabra mágica **`juan`**.
- **Voz Neuronal Humana**: En lugar de sonar como un robot de los años 90, Juan utiliza las voces neuronales de Microsoft Edge (`edge-tts`). Responde de manera fluida y con acento natural, haciendo comentarios amigables (ej. *"Claro que sí, abriendo la calculadora para ti"*).

## 🪟 2. Control Total de Aplicaciones Windows
Juan puede interactuar con los programas instalados en tu computadora. Puedes pedirle que:
- **Abra aplicaciones:** `"Juan, abre word"`, `"Juan, abre discord"`, `"Juan, abre la configuración"`, `"Juan, abre paint"`.
- **Cierre aplicaciones:** `"Juan, cierra notepad"`.
- **Minimice ventanas:** `"Juan, minimiza chrome"` (oculta la ventana en la barra de tareas).
- **Maximice ventanas:** `"Juan, maximiza chrome"` (restaura la ventana para que ocupe toda la pantalla).

## 🌐 3. Navegación Web y Automatización
Gracias a la librería Playwright, Juan toma el control de un navegador Chromium visible para ti:
- **Búsquedas en Google:** `"Juan, busca en google recetas de cocina"`. Juan abrirá el navegador, escribirá tu búsqueda y presionará Enter automáticamente.
- **Búsquedas en YouTube:** `"Juan, busca en youtube tutoriales de programación"`. Juan entrará directo a YouTube y buscará los videos.
- **Abrir páginas populares:** `"Juan, abre facebook"`, `"Juan, abre netflix"`. Entrará directamente a la URL `facebook.com` o `netflix.com`.

## 🔊 4. Control del Sistema y Multimedia
Puedes pedirle a Juan que controle el hardware y sistema operativo de tu PC:
- **Subir/Bajar volumen:** `"Juan, sube el volumen"`, `"Juan, baja el volumen"`.
- **Silenciar (Mute):** `"Juan, silencia el equipo"`.
- **Control de Música (Spotify, YouTube, etc):** `"Juan, pon música"` (Play/Pause), `"Juan, siguiente canción"`, `"Juan, canción anterior"`.
- **Captura de pantalla:** `"Juan, toma una captura de pantalla"`. (Guardará la foto como `captura_jarvis.png` en la carpeta de Python).
- **Seguridad:** `"Juan, bloquea la pantalla"`. (Cerrará tu sesión activa de Windows bloqueando el equipo instantáneamente).

## ⏰ 5. Asistencia Diaria
Juan es consciente de su entorno temporal:
- **Hora exacta:** `"Juan, qué hora es"`. (Te dirá la hora actual formateada de forma natural: "Son las 3:15 PM").
- **Fecha exacta:** `"Juan, qué día es"`. (Te dirá la fecha: "Hoy es 1 de julio de 2026").

## 🧠 6. Aprendizaje y Memoria (Alias)
Juan tiene la capacidad de aprender cómo te gusta llamar a tus aplicaciones:
- **Asignación de sinónimos:** Si tienes un juego llamado "Juego.exe" y quieres decirle "abre mi juego", puedes decirle `"Juan, aprende mi juego como Juego.exe"`. Su memoria (gestionada en Java) guardará esto, y la próxima vez que digas `"Juan, abre mi juego"`, él sabrá qué hacer.

## 💻 7. Dashboard Cyberpunk (Panel de Control)
Si no puedes o no quieres usar la voz, tienes un Panel Web interactivo:
- **Canal Seguro de Texto:** Puedes escribir comandos (ej. `"abre youtube"`) y presionar "Transmitir Orden".
- **Botones de Acción Rápida (Macros):** Una cuadrícula de botones para acciones instantáneas: un click para buscar música, un click para silenciar, un click para ver la hora o bloquear la pantalla.
- **Consola de Registro en Vivo:** Un terminal visual que te muestra en tiempo real lo que escuchas, lo que interpreta Java y las acciones de sistema que se ejecutan, dándote visibilidad 100% de los procesos de la IA.

---

### 🚀 Cómo Inicializar Todo el Sistema (El Ritual de Encendido)
Para que todo este ecosistema funcione a la perfección, los tres pilares deben estar activos:
1. Dale **Run / Play** al servidor Spring Boot en **Eclipse** (El Cerebro).
2. Abre la terminal, ve a `d:/skinet/python-daemon/` y ejecuta **`python main.py`** (El Sistema Nervioso y el Micrófono).
3. Abre el archivo **`d:/skinet/4-dashboard-rostro/index.html`** en Chrome u otro navegador (El Rostro).
