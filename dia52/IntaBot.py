from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time




SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow
USERNAME = "juandinegrete2006@outlook.com"       # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = "xpUAq2khmioW0KbO"   
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollowerBot:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self):
        self.driver.get(LOGIN_URL)
        email_input=self.driver.find_element(By.XPATH,"//*[@id='username']")
        password_input=self.driver.find_element(By.XPATH,"//*[@id='password']")
        email_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)

        boton_login=self.driver.find_element(By.XPATH,"/html/body/div/div/form/button")
        boton_login.click()

        time.sleep(1)
        boton_guardar_sesion=self.driver.find_element(By.XPATH,"//*[@id='popup-save-login']/div/div[2]")
        boton_guardar_sesion.click()

        time.sleep(1)
        boton_aceptar_cookies=self.driver.find_element(By.XPATH,"//*[@id='popup-notifications']/div/button[2]")
        boton_aceptar_cookies.click()
        
    def find_followers(self):
        search_button=self.driver.find_element(By.XPATH,"/html/body/div[1]/nav/button")
        search_button.click()
        time.sleep(1)
        profile_input=self.driver.find_element(By.XPATH,"/html/body/aside/div[4]/a[1]")
        profile_input.click()
        followers_button=self.driver.find_element(By.XPATH,"/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a")
        followers_button.click()
        
    def follow(self):
       time.sleep(2)
       follow_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow') or contains(text(), 'Seguir')]")
       for button in follow_buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
            except:
                button.click()
                time.sleep(1)

bot=InstaFollowerBot(webdriver.Chrome())
bot.login()
bot.find_followers()
bot.follow()

time.sleep(40)