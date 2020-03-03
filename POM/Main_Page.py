from POM import Page
from POM.Header_Section import Header_Section
from POM.Nav_Menu import Nav_Menu


class Main_Page(Page):
    def start(self):
        self.url =""
        self.open(self.url)
        self.header_obj = Header_Section(self.driver)
        self.menu_obj =Nav_Menu(self.driver)

        
