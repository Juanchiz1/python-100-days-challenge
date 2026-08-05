from selenium import webdriver
from selenium.webdriver.common.by import By
# 1. Importar la clase que gestiona los drivers
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Inicialización del driver de forma automática y segura
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

# Ahora puedes ejecutar tu código sin problemas de ubicación/versión
driver.get("https://en.wikipedia.org/wiki/Main_Page")
price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_cents=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.close()

