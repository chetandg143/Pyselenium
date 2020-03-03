import unittest

from selenium import  webdriver

from Prpom.Driver import drivers


class Shopping_page:



        drivers.get("http://www.amazon.com/")
        print(drivers.title)
        drivers.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Redmi note 8 Pro")
        drivers.find_element_by_xpath("//input[@type='submit']").click()

        print(drivers.title)



