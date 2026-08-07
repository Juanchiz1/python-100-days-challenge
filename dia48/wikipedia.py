
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles=driver.find_element(By.XPATH,value='//*[@id="mwDw"]')
print(articles.text)

#articles.click()

all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")
#all_portals.click()


search_button = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
search_button.click()

time.sleep(1)

search = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input')
search.send_keys("Python programming language")
search.send_keys(Keys.ENTER)