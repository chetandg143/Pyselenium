from selenium import  webdriver


from locators import MainPageLocators


class BasePageElement(object):
    pass


class SearchTextElement(BasePageElement):
    locator = 'q'


class MainPageLocator(object):
    pass


class BasePage(object):
    pass


class BasePage(object):
    def __int__(self,driver):
        self.driver =webdriver.Chrome(executable_path='/home/tibil/Chetan/chromedriver_linux64/chromedriver')

    class MainPage(BasePage):
        search_text_element =SearchTextElement()

        def is_title_matches(self):
            return "Python" in self.driver.title

        def click_go_button(self):
            element = self.driver.find_elment(*MainPageLocator.GO_BUTTON)
            element.click()

    class SearchResultsPage(BasePage):
        def is_result_found(self):
            return "No results found" not in self.driver.page_source
