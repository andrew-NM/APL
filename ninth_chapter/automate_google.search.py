from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Python Web Scraping")
search.send_keys(Keys.RETURN)
print(driver.title())
driver.quit()