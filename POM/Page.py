import logging
import time
import unittest


class Base_Logging(object):
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything


class Page(unittest.TestCase):
    def __init__(self,driver ,base_url='https://www.google.com/'):
        if base_url[-1]!= '/':
            base_url += '/'
        self.base_url = base_url
        self.driver = driver
        self.start()
        self.log_obj = Base_Logging(level=logging.DEBUG)

    def open(self ,url):
        url =self.base_url + url
        self.driver.get(url)

    def get_xpath(self , xpath):
        "Return the DOM element of the xpath OR the 'None' object if the element"

    def get_xpath(self , xpath):
          "Return the DOM element of the xpath OR the 'None' object if the element"

    def click_element(self ,xpath):
        "click the button supplied"

    def write(self,msg,level='info'):
        self.log_obj.write(msg,level)

    def wait(self ,wait_seconds=5):
        time.sleep(wait_seconds)
