import unittest
# from SeleniumPythonRefactorTestCase import SearchText
# from SeleniumPythonMultipleTests import search

# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase()
home_page_test = unittest.TestLoader().loadTestsFromTestCase()

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)