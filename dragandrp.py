import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')
driver.maximize_window()
driver.get("http://jqueryui.com/droppable/")
driver.switch_to_frame(0)
source_element = driver.find_element_by_id("draggable")
dest_element = driver.find_element_by_id("droppable")
actions = ActionChains(driver)
actions.drag_and_drop(source_element, dest_element).perform()
print(dest_element.text)

driver.quit()