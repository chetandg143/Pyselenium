
import unittest
from selenium import webdriver

class Tes(unittest):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/tibil/chetan/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()

        self.driver.get("http:www.faceboook.com")
