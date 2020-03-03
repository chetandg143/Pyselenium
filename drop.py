from selenium import webdriver
from selenium.webdriver import ActionChains

driver =webdriver.Chrome("/home/tibil/Chetan/chromedriver_linux64/chromedriver")
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")

driver.switch_to_frame(0)
src =driver.find_element_by_id("draggable")

actions = ActionChains(driver)
actions.drag_and_drop_by_offset(src ,100 ,100).perform()