
import unittest
from  selenium import webdriver
class Searchtext:
    def setUp(self):
        self.driver =webdriver.Chrome(executable_path="/home/tibil/Chetan/chromedriver_linux64/chromedriver")

        self.driver.get("http://www.facebook.com")

        def tearDown(self):
            self.driver.quit()