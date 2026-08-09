from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        """Obtiene velocidad con múltiples estrategias para el botón"""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        
        # Esperar a que la página cargue completamente
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Intentar hacer clic en el botón Go
        if not self._click_go_button():
            print("❌ No se pudo hacer clic en el botón Go")
            return
        
        # Esperar que termine la prueba
        print("⏳ Esperando resultados de la prueba de velocidad...")
        time.sleep(70)  # Ajusta según tu velocidad
        
        # Obtener resultados
        try:
            # Velocidad de descarga
            down_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='download-speed']"))
            )
            self.down = float(down_element.text)
            
            # Velocidad de subida
            up_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='upload-speed']"))
            )
            self.up = float(up_element.text)
            
            print(f"✅ Velocidad obtenida: {self.down} down / {self.up} up")
            
        except Exception as e:
            print(f"❌ Error al obtener velocidades: {e}")
            self.down = 100  # Valores por defecto
            self.up = 100
    
    def _click_go_button(self):
        """Método interno para hacer clic en el botón Go"""
        
        # Lista de estrategias a probar
        strategies = [
            # Estrategia 1: Por clase principal
            (By.CLASS_NAME, "start-text"),
            # Estrategia 2: Por XPath con texto
            (By.XPATH, "//span[contains(text(), 'GO') or contains(text(), 'Ir')]"),
            # Estrategia 3: Por XPath con clase
            (By.XPATH, "//*[contains(@class, 'start')]"),
            # Estrategia 4: Por XPath con ID (si existe)
            (By.XPATH, "//*[@id='start']"),
            # Estrategia 5: Por selector CSS
            (By.CSS_SELECTOR, ".start-button, .js-start-test, .test-button"),
        ]
        
        for by, value in strategies:
            try:
                print(f"🔍 Intentando: {by} = {value}")
                button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((by, value))
                )
                
                # Scroll hasta el botón para asegurar visibilidad
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(0.5)
                
                # Intentar clic normal
                button.click()
                print(f"✅ Botón clickeado exitosamente usando: {by}")
                return True
                
            except (TimeoutException, ElementClickInterceptedException) as e:
                print(f"⚠️ Falló estrategia {by}: {str(e)[:50]}")
                continue
        
        # Último recurso: JavaScript
        try:
            print("🔄 Intentando clic con JavaScript...")
            self.driver.execute_script("""
                var elements = document.querySelectorAll('button, a, div[role="button"]');
                for (var i = 0; i < elements.length; i++) {
                    var text = elements[i].textContent || elements[i].innerText;
                    if (text && (text.toUpperCase().includes('GO') || text.toUpperCase().includes('IR'))) {
                        elements[i].click();
                        return true;
                    }
                }
                return false;
            """)
            print("✅ Clic con JavaScript exitoso")
            return True
        except:
            print("❌ Todas las estrategias fallaron")
            return False

# 🚀 Código de ejecución
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    bot = InternetSpeedTwitterBot(driver)
    bot.get_internet_speed()
    
    time.sleep(5)
    driver.quit()