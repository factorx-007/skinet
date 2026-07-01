# GUÍA DE PROYECTO: Asistente Virtual Autónomo

## 1. Objetivo Principal
Crear un asistente virtual único, con nombre propio, capaz de interactuar de forma natural y conversacional con el usuario a través de comandos de voz. El asistente debe ser capaz de controlar el entorno del sistema operativo, manipular navegadores de forma avanzada, aprender gradualmente las preferencias del usuario y adaptar sus respuestas para ofrecer una experiencia altamente personalizada.

---

## 2. Estructura de Carpetas y Módulos Independientes
Para mantener el código organizado, escalable y mantenible, el proyecto se divide estrictamente en módulos independientes separados en carpetas.

### Carpeta `python-daemon` (Control de Hardware y Sistema)
Encargada de interactuar físicamente con el equipo (micrófono, altavoces, sistema operativo, navegador).
* **`reconocimiento_voz/`**: Captura pasiva del micrófono, detección de la palabra de activación (Ej. "Jarvis" o "Hola sistema") y conversión de Voz a Texto (STT).
* **`sintesis_voz/`**: Conversión de Texto a Voz (TTS) para darle una voz natural y única al asistente.
* **`control_sistema/`**: Scripts de automatización del sistema operativo (Windows). Ejecuta la apertura, cierre, maximización y minimización de aplicaciones nativas.
* **`control_navegador/`**: Módulo avanzado (utilizando librerías como Selenium, Playwright o PyAutoGUI) dedicado a manipular Google Chrome u otros navegadores, permitiendo búsquedas, clics y selecciones.

### Carpeta `java-core` (El Cerebro y Lógica de Negocio)
Encargada de pensar, procesar el lenguaje natural, recordar al usuario y tomar decisiones.
* **`procesamiento_nlp/`**: Analiza el texto recibido de Python, identifica la "intención" del usuario (saludo, orden, pregunta) y extrae las variables clave.
* **`memoria_personalizacion/`**: Conexión a la base de datos (H2/PostgreSQL). Guarda perfiles de usuario, alias de comandos, preferencias y analiza el uso frecuente para "aprender".
* **`servicios_futuros/`**: Preparado para integraciones externas (APIs de clima, Spotify, Smart Home, etc.).

---

## 3. Detalle de Funciones Esenciales

### A. Reconocimiento de Voz e Interacción Natural
* **Activación por Nombre**: El asistente siempre está escuchando en segundo plano, pero solo despierta al escuchar su nombre o palabra clave de activación.
* **Saludos y Despedidas Flexibles**: Entiende múltiples formas de saludar ("Buenos días", "Hola", "¿Qué tal?") y responderá de forma variada para evitar ser robótico.
* **Personalidad**: Tendrá respuestas adaptativas y podrá usar el nombre del usuario.

### B. Control de Aplicaciones (Sistema Operativo)
El asistente tiene control total sobre las ventanas de Windows.
* **5 Aplicaciones Base Garantizadas**:
  1. Google Chrome / Navegador Web
  2. Explorador de Archivos
  3. Calculadora
  4. Bloc de Notas / Editor de Texto
  5. Terminal / CMD
* **Acciones soportadas**: "Abrir", "Cerrar", "Minimizar", "Maximizar", "Traer al frente".

### C. Automatización Avanzada de Google (Navegador)
Esta función va mucho más allá de simplemente "abrir Chrome".
* **Búsquedas de Voz Inteligentes**: "Busca en Google noticias de hoy" -> El asistente abre Chrome, va a Google, escribe la búsqueda y presiona Enter.
* **Navegación Interactiva**: Permite comandos como:
  * "Haz scroll hacia abajo" o "Baja la página".
  * "Abre la primera página de los resultados".
  * "Cierra esta pestaña".
  * "Ve a YouTube y busca música relajante".
* **Selección por Voz**: Usando técnicas de accesibilidad o inyección de scripts, el asistente podrá identificar enlaces en pantalla y permitirle al usuario decir "Haz clic en el enlace de Wikipedia" sin tocar el ratón.

### D. Personalización y Aprendizaje Automático
* **Aprendizaje Gradual**: El sistema registrará las acciones más repetidas. Si el usuario dice siempre "Pon música" y luego abre Spotify, el asistente aprenderá que "Pon música" = "Abrir Spotify" para este usuario en particular.
* **Alias Personalizados**: El usuario podrá enseñarle comandos en tiempo real: *"Cuando diga 'Hora de trabajar', abre Word y Chrome"*.
* **Adaptación de Tono**: Si el usuario usa lenguaje formal o abreviado, el asistente puede ajustar su nivel de verbosidad (respuestas más largas o más cortas).

---

## 4. Ampliación de Funcionalidades (Roadmap a Futuro)
El sistema está diseñado de forma modular para que agregar esto sea tan fácil como añadir un nuevo plugin:
1. **Búsqueda Avanzada en Internet**: Scraping en tiempo real para leerle al usuario el primer párrafo de Wikipedia o el clima actual.
2. **Reproducción de Música**: Integración con la API de Spotify para buscar canciones, pausar, reproducir o cambiar de pista sin abrir la ventana.
3. **Control de Dispositivos Inteligentes (Domótica)**: Envío de peticiones web (HTTP/MQTT) para apagar/encender luces inteligentes, aires acondicionados o enchufes (Smart Home).
4. **Recordatorios y Alarmas**: El usuario dirá *"Recuérdame apagar el horno en 20 minutos"*, el asistente creará un cronograma en Java y emitirá una alerta visual y auditiva cuando se cumpla el plazo.
