import time

from selenium.webdriver.support.select import Select

from Prpom.Driver import drivers

from Prpom import loginpage
class Address:
    print(drivers.title)
    drivers.find_element_by_id("enterAddressFullName").clear()
    drivers.find_element_by_id("enterAddressFullName").send_keys("Chetan D Goudar")
    drivers.find_element_by_id("enterAddressAddressLine1").send_keys("Tibil solutions kadubeesanahalli ")
    drivers.find_element_by_id("enterAddressCity").send_keys("Bangalore")
    drivers.find_element_by_id("enterAddressStateOrRegion").send_keys("Karnataka")
    drivers.find_element_by_id("enterAddressPostalCode").send_keys("560103")
    ele =Select(drivers.find_element_by_id("enterAddressCountryCode"))
    ele.select_by_visible_text("India")
    drivers.find_element_by_id("enterAddressPhoneNumber").clear()
    drivers.find_element_by_id("enterAddressPhoneNumber").send_keys("7829652460")
    drivers.find_element_by_id("GateCode").send_keys("143")
    time.sleep(5)
   # drivers.find_element_by_xpath("//*[@id='addres-new']/div/form/div[6]/label[2]/input").click()
    drivers.find_element_by_xpath("//input[@value='Continue']").click()
    drivers.save_screenshot("adress.png")

    time.sleep(2)
    drivers.find_element_by_id("addr_0").click()