import subprocess
import psutil
import pygetwindow as gw
import os

class OSController:
    def __init__(self):
        # Mapeo básico de aplicaciones comunes en Windows
        self.app_map = {
            "chrome": "chrome.exe",
            "google": "chrome.exe",
            "google chrome": "chrome.exe",
            "navegador": "chrome.exe",
            "bloc de notas": "notepad.exe",
            "notepad": "notepad.exe",
            "calculadora": "calc.exe",
            "calc": "calc.exe",
            "explorador": "explorer.exe",
            "explorador de archivos": "explorer.exe",
            "archivos": "explorer.exe",
            "spotify": "spotify.exe"
        }

    def _clean_name(self, name):
        name = name.lower().strip()
        for article in ["la ", "el ", "los ", "las ", "un ", "una "]:
            if name.startswith(article):
                name = name[len(article):].strip()
                break
        return name

    def open_app(self, app_name_or_alias):
        name = self._clean_name(app_name_or_alias)
        target_exe = self.app_map.get(name, name)
        try:
            print(f"[OS] Abriendo {target_exe}...")
            # En Windows, usar start para que busque en el PATH
            subprocess.Popen(f"start {target_exe}", shell=True)
            return True, f"Abriendo {app_name_or_alias}"
        except Exception as e:
            print(f"[OS] Error abriendo {target_exe}: {e}")
            return False, f"Error al abrir {app_name_or_alias}"

    def close_app(self, app_name_or_alias):
        name = self._clean_name(app_name_or_alias)
        target_exe = self.app_map.get(name, name)
        closed = False
        try:
            print(f"[OS] Cerrando {target_exe}...")
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] and proc.info['name'].lower() == target_exe.lower():
                    proc.kill()
                    closed = True
            if closed:
                return True, f"{app_name_or_alias} cerrado."
            else:
                return False, f"No encontré {app_name_or_alias} en ejecución."
        except Exception as e:
            print(f"[OS] Error cerrando {target_exe}: {e}")
            return False, f"Error al cerrar {app_name_or_alias}"

    def _find_window_by_name(self, name):
        windows = gw.getWindowsWithTitle(name)
        if not windows:
            all_windows = gw.getAllWindows()
            for w in all_windows:
                if name.lower() in w.title.lower():
                    return w
        elif len(windows) > 0:
            return windows[0]
        return None

    def minimize_app(self, app_name_or_alias):
        name = self._clean_name(app_name_or_alias)
        window = self._find_window_by_name(name)
        if window:
            window.minimize()
            return True, f"Minimizando {app_name_or_alias}"
        return False, f"No encontré la ventana de {app_name_or_alias}"

    def maximize_app(self, app_name_or_alias):
        name = self._clean_name(app_name_or_alias)
        window = self._find_window_by_name(name)
        if window:
            window.maximize()
            return True, f"Maximizando {app_name_or_alias}"
        return False, f"No encontré la ventana de {app_name_or_alias}"

if __name__ == "__main__":
    import time
    os_ctrl = OSController()
    os_ctrl.open_app("notepad")
    time.sleep(3)
    os_ctrl.minimize_app("notepad")
    time.sleep(2)
    os_ctrl.maximize_app("notepad")
    time.sleep(2)
    os_ctrl.close_app("notepad")
