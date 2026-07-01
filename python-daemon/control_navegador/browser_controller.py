import threading
import time
from playwright.sync_api import sync_playwright

class BrowserController:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        
    def _start_browser(self):
        if self.playwright is None:
            self.playwright = sync_playwright().start()
        # Launching visibly (headless=False)
        if self.browser is None:
            self.browser = self.playwright.chromium.launch(headless=False)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()

    def ensure_browser_open(self):
        if not self.browser:
            print("[BROWSER] Iniciando navegador Playwright...")
            self._start_browser()
            return "Navegador abierto."
        return "El navegador ya está abierto."

    def search_google(self, query):
        try:
            self.ensure_browser_open()
            print(f"[BROWSER] Buscando en Google: {query}")
            self.page.goto("https://www.google.com")
            # Fill the search box. Playwright handles the input automatically by locator
            search_input = self.page.locator('textarea[name="q"], input[name="q"]')
            search_input.fill(query)
            search_input.press("Enter")
            self.page.wait_for_load_state("networkidle")
            return True, f"Buscando {query} en Google."
        except Exception as e:
            print(f"[BROWSER] Error al buscar: {e}")
            return False, f"Error al buscar en Google."

    def close_browser(self):
        if self.browser:
            self.browser.close()
            self.browser = None
        if self.playwright:
            self.playwright.stop()
            self.playwright = None
        return True, "Navegador cerrado."

if __name__ == "__main__":
    bc = BrowserController()
    bc.search_google("noticias de tecnología")
    time.sleep(5)
    bc.close_browser()
