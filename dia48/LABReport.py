
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name = driver.find_element(By.XPATH, value='//*[@id="signup-form"]/input[1]')
first_name.send_keys("John")
last_name = driver.find_element(By.XPATH, value='//*[@id="signup-form"]/input[2]')
last_name.send_keys("Doe")
email = driver.find_element(By.XPATH, value='//*[@id="signup-form"]/input[3]')
email.send_keys("juanchiz@gmail.com")

sign_up_button = driver.find_element(By.XPATH, value='//*[@id="signup-form"]/button')
sign_up_button.click()