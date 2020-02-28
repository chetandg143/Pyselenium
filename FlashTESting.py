import time

import selenium.webdriver


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')
driver.maximize_window()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


driver.close()