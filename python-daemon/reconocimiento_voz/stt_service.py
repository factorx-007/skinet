import speech_recognition as sr
import threading
import time

class STTService:
    def __init__(self, wake_words=["juan"], callback=None):
        self.recognizer = sr.Recognizer()
        self.wake_words = [w.lower() for w in wake_words]
        self.callback = callback
        self.is_listening = False
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            print("[STT] Calibrando para ruido de fondo...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("[STT] Calibración completa.")

    def start_listening(self):
        self.is_listening = True
        self._listen_thread = threading.Thread(target=self._listen_loop, daemon=True)
        self._listen_thread.start()

    def stop_listening(self):
        self.is_listening = False

    def _listen_loop(self):
        print(f"[STT] Escuchando activamente. Wake words permitidas: {self.wake_words}")
        print("[STT] Di primero 'juan' y luego tu comando (ej: 'juan abre la calculadora').")
        while self.is_listening:
            with self.microphone as source:
                try:
                    # Escucha una frase corta
                    print("[STT] (Micrófono abierto, esperando voz...)")
                    audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    print("[STT] Procesando audio con Google Speech Recognition...")
                    
                    text = self.recognizer.recognize_google(audio, language="es-ES").lower()
                    print(f"[STT] Escuchado: '{text}'")
                    
                    detected_word = next((w for w in self.wake_words if w in text), None)
                    if detected_word:
                        # Extraer comando después del wake word
                        command = text.split(detected_word, 1)[-1].strip()
                        if command and self.callback:
                            self.callback(command)
                        elif not command and self.callback:
                            print("[STT] Wake word detectado. Escuchando comando inmediatamente...")
                            try:
                                audio_cmd = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
                                print("[STT] Procesando comando de voz...")
                                cmd_text = self.recognizer.recognize_google(audio_cmd, language="es-ES").lower()
                                print(f"[STT] Comando detectado: '{cmd_text}'")
                                self.callback(cmd_text)
                            except:
                                print("[STT] No se detectó comando después del wake word.")
                    else:
                        print(f"[STT] Se escuchó '{text}', pero no contiene ninguna palabra clave de activación. Ignorando.")
                            
                except sr.WaitTimeoutError:
                    # Timeout normal sin habla, no mostramos error para no inundar la consola
                    pass
                except sr.UnknownValueError:
                    print("[STT] 🎙️ Audio detectado pero no se entendieron las palabras (Intenta hablar más claro o revisa el volumen del micro).")
                except sr.RequestError as e:
                    print(f"[STT] ❌ Error de red con el servicio de reconocimiento de Google: {e}")
                except Exception as e:
                    print(f"[STT] ❌ Error inesperado: {e}")
            time.sleep(0.1)

if __name__ == "__main__":
    def on_command(cmd):
        print(f"Comando recibido: {cmd}")
    
    stt = STTService(callback=on_command)
    stt.start_listening()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stt.stop_listening()
