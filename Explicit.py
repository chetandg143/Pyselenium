import time

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')
driver.get('http://gmail.com/')
driver.maximize_window()
try:

 element = WebDriverWait(driver , 10).until(
     EC.presence_of_element_located((By.Type,"email").count())
 )

finally:
    time.sleep(200)