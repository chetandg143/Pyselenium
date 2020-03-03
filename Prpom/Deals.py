import time

from Prpom import Shopping
from Prpom.Driver import drivers


class Dealers:
    drivers.save_screenshot("deals.png")
    drivers.find_element_by_xpath("//div[@class='a-section aok-relative s-image-fixed-height']/img[@data-image-index='0']").click()

    drivers.save_screenshot("second.png")
    price = drivers.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
    print("price of mobile is ",price)
    details = drivers.find_element_by_xpath("//div[@id='feature-bullets']").text
    print(details)
    drivers.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
    


