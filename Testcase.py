import unittest

from selenium import webdriver
import page

#
#
# class PythonorgSearch(unittest.TestCase):
#
#     def SetUp(self):
#         self.driver =webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')
#         self.driver.get('http://www.python.org')
#
#     def test_search_in_python(self):
#
#         main_page = page.MainPage(self.driver)
#         assert main_page.is_title_matches() , "python.org does not match"
#
#         main_page.search_text_element = 'pycon'
#         main_page.click_go_button()
#         search_results_page = page.SearchResultsPage(self.driver)
#         assert  search_results_page.is_results_found() , " no result found!."
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):

        main_page = page.MainPage(self.driver)

        assert main_page.is_title_matches(), "python.org title doesn't match."

        main_page.search_text_element ="pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)

        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()