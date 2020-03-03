from POM import Page

class Nav_Menu(Page):
    "page object for the side menu "

    def start(self):
        self.inbox =""
        self.sent_mail=""
        self.drafts=""

    def select_menu_item(self ,menu_item):
        "select menu items "
        