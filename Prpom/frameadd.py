import time

from selenium.webdriver.support.select import Select

from Prpom.Driver import drivers
from Prpom import addtocart
from selenium.webdriver import ActionChains
class addtoorder:
    drivers.find_element_by_xpath("//input[@id='sc-buy-box-gift-checkbox']").click()
    drivers.find_element_by_xpath("//input[@name='proceedToRetailCheckout']").click()
    print(drivers.title)

