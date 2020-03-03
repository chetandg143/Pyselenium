import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/home/tibil/Chetan/chromedriver_linux64/chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.facebook.com/")
print(driver.current_url)
print(driver.title)
driver.find_element_by_xpath("//input[@name='firstname']").send_keys("Uday")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("N")

driver.find_element_by_xpath("//input[@name='reg_email__']").send_keys("8217584292")
driver.find_element_by_xpath("//input[@name='reg_passwd__']").send_keys("2924857128")

select_days =Select(driver.find_element_by_id("day"))
select_days.select_by_value('4')
# print("Days from 1 to 31 ")
# for i in range(len(select_days)):
#     print(select_days[i].text)


select_months = Select(driver.find_element_by_id("month"))
select_months.select_by_visible_text('Apr')
# for i in range(len(select_months)):
#     print(select_months[i].text)

select_years =Select(driver.find_element_by_id("year"))
select_years.select_by_value('1996')
# for  i in range(len(select_years)):
#     print(select_years[i].text)


driver.find_element_by_xpath("//input[@value='2']").click()


driver.find_element_by_xpath("//button[@name='websubmit']").click()

time.sleep(5000)
move = driver.find_elements_by_id("userNavigationLabel")
action = ActionChains(move)
action.click()

driver.find_element_by_xpath("//li[@class='_54ni navSubmenu _6398 _64kz __MenuItem']/a[@class='_54nc']").click()
