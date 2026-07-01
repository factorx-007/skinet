import os
import subprocess
import pygame
import time

class TTSService:
    def __init__(self, voice="es-MX-JorgeNeural"):
        self.voice = voice
        pygame.mixer.init()
        
    def speak(self, text):
        print(f"[TTS] Diciendo: {text}")
        output_file = "response.mp3"
        
        # Generar el audio usando edge-tts CLI
        try:
            subprocess.run([
                "edge-tts", 
                "--voice", self.voice, 
                "--text", text, 
                "--write-media", output_file
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Reproducir el audio
            pygame.mixer.music.load(output_file)
            pygame.mixer.music.play()
            
            # Esperar a que termine de reproducirse
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            # Liberar el archivo
            pygame.mixer.music.unload()
            
            # Eliminar el archivo de audio para que no se acumule
            if os.path.exists(output_file):
                os.remove(output_file)
                
        except Exception as e:
            print(f"[TTS] Error al generar/reproducir voz: {e}")

if __name__ == "__main__":
    tts = TTSService()
    tts.speak("Hola, soy Juan. Inicializando módulo de voz neuronal.")
