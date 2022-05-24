from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
driver.close()