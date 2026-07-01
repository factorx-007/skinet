# 🤖 Proyecto: Asistente Virtual Personalizado

## 📌 Objetivo
Desarrollar un asistente virtual escalable con reconocimiento de voz, control de sistema operativo y capacidad de aprendizaje. 

## 🏗️ Arquitectura del Sistema (Microservicios)
* **Daemon/Hardware (Python 3.10+):** Procesamiento de audio, STT, TTS y ejecución de procesos del SO local.
* **Core Lógico (Java 17+ / Spring Boot):** Base de datos, NLP básico, historial, personalización y enrutador de comandos.
* **Frontend (HTML5 / CSS3 / Vanilla JS):** Dashboard local SPA para configuración y monitoreo del estado.
* **Comunicación:** JSON vía WebSockets (recomendado para baja latencia) o API REST local.

---

## 🚀 Plan de Ejecución Paso a Paso

### 🛠️ Fase 1: Configuración Base y Protocolo
- [ ] Definir el contrato de comunicación JSON (Ej: `{"source": "voice", "intent": "OPEN_APP", "target": "chrome"}`).
- [ ] Inicializar repositorio y crear la estructura de carpetas (separando proyectos de Python, Java y Web).
- [ ] Levantar un servidor Spring Boot vacío con endpoints de prueba.

### 🐍 Fase 2: Módulo Python (Oído y Mano)
- [ ] **STT (Speech-to-Text):** Implementar `SpeechRecognition` o `Vosk`. Configurar un *Wake Word* pasivo (ej. "Hola Sistema") para activar la escucha real.
- [ ] **TTS (Text-to-Speech):** Implementar `pyttsx3` para las respuestas de voz (configurar velocidad y voz en español).
- [ ] **Control del OS:** Crear un script usando `subprocess` y `psutil`.
- [ ] Mapear y testear el inicio y cierre de **5 aplicaciones mínimas**:
    - [ ] 🌐 Navegador (`chrome.exe` / `msedge.exe`)
    - [ ] 📝 Bloc de notas (`notepad.exe`)
    - [ ] 🧮 Calculadora (`calc.exe`)
    - [ ] 📁 Explorador de archivos (`explorer.exe`)
    - [ ] 🎵 Reproductor (`spotify.exe` o equivalente)

### ☕ Fase 3: Módulo Java (Cerebro y Base de Datos)
- [ ] **Setup DB:** Configurar conexión H2 (embebida) o PostgreSQL en Spring Boot usando JPA/Hibernate.
- [ ] **Entidades:** Crear tablas `Usuario`, `ComandoAlias` (para personalización) e `HistorialInteraccion`.
- [ ] **NLP Básico:** Implementar una clase que reciba el texto de Python, lo normalice (minúsculas, sin tildes) y extraiga la "Intención" (Ej: Abrir, Cerrar).
- [ ] **Motor de Aprendizaje:** Crear la lógica donde, si un comando no se reconoce, pida el alias al usuario, lo guarde en DB y lo resuelva automáticamente en el futuro.

### 🌐 Fase 4: Módulo UI (Rostro y Configuración)
- [ ] **Maquetación HTML:** Crear estructura semántica (`<header>`, `<section id="terminal-log">`, `<section id="app-manager">`).
- [ ] **Estilos CSS:** Aplicar CSS Grid y Flexbox. Configurar variables nativas (`:root`) para un *Dark Mode* profesional.
- [ ] **Integración JS:** Conectar el Dashboard con Spring Boot (Fetch API) para mostrar el historial en tiempo real y permitir editar las rutas de las apps o el nombre del usuario.

### 📈 Fase 5: Expansión (Mantenimiento Backend)
*(Implementar solo cuando el flujo Voz -> Python -> Java -> Python esté pulido).*
- [ ] **Búsqueda Web:** Usar `JSoup` en Java para scrapear respuestas rápidas (ej. primer párrafo de Wikipedia) y enviarlas al TTS de Python.
- [ ] **Recordatorios:** Integrar `Quartz Scheduler` o hilos en Java para disparar alertas temporales hacia Python.
- [ ] **IoT:** Preparar `RestTemplate` o `WebClient` en Java para consumir APIs externas (luces inteligentes, etc.).

---

## 💾 Diccionario de Datos (Ejemplo Payload)
**Python a Java (Request):**
```json
{
  "timestamp": "2026-06-30T21:12:00",
  "raw_text": "abre el navegador por favor"
}