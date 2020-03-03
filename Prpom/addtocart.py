import time

from Prpom.Driver import drivers
from Prpom import Deals
class add_card:
    time.sleep(2)
    drivers.find_element_by_xpath("//span[@class='a-button-inner']/a[@id='hlb-view-cart-announce']").click()
    print(drivers.title)

