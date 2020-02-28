import os

from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox(executable_path = '/home/tibil/Chetan/geckodriver-v0.26.0-linux64/geckodriver')
driver =webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

lists = driver.find_element_by_class_name("r")

print("Found " + str(len(lists)) + " searches:")

i = 0;
for lstitem in lists:
    print(lstitem.get_attribute("innerHTML"))
    i =i+1
    if(i> 10):
        break

driver.quit()

#
# ele = driver.find_element_by_id('email')
# ele.send_keys('chetandg143@gmail.com')
#
# ele = driver.find_element_by_id('pass')
# ele.send_keys('')
# #ele.send_keys(Keys.RETURN)
# #ele = driver.find_element_by_id('loginbutton').click()
# print(driver.current_url)
# print(driver.page_source)
# print(driver.get_screenshot_as_base64())
# print( driver.get_screenshot_as_file('/home/tibil/Desktop/pc.png'))
# print(driver.get_screenshot_as_png())
# print(driver.get_window_size( ))
# driver. minimize_window()
# print(driver.save_screenshot("/home/tibil/d.png"))