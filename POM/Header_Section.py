from POM import Page

class Header_Section(Page):
    def start(self):

        self.search_txtbox =""
        self.search_btn =""
        self.sign_out =""
        self.search_result =""

    def search_by_subject(self ,serachtxt):
        self.set_txt(self.search_txtbox,'subject: '+serachtxt)
        