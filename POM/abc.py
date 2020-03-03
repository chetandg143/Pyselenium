

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')
driver.maximize_window()
driver.get("http://www.google.com")
