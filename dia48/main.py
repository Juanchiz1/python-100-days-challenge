from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

#price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole").text
#price_cents=driver.find_element(By.CLASS_NAME,value="a-price-fraction").text
#print(f"The price is ${price_dollar}.{price_cents}")

search_bar=driver.find_element(By.NAME,value="q")
print(search_bar.tag_name)
button=driver.find_element(By.ID,value="submit")
print(button.size)
documentation_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(documentation_link.text)

bug_link=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[2]/p[2]/a')
print(bug_link.text)

