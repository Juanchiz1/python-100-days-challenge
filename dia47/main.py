from selenium import webdriver
# 1. Importar la clase que gestiona los drivers
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Inicialización del driver de forma automática y segura
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

# Ahora puedes ejecutar tu código sin problemas de ubicación/versión
driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.close()