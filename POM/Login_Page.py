from POM import Page
from POM.DriverFactory import driver


class Login_Page(Page):
    def start(self):
        self.url =""
        self.open(self.url)
        self.assertIn("Gmail" , self.driver.title)

        #login credentials
        self.sign_in =driver.find_element_by_xpath("//a[@data-pid=23]").click()
        self.login_email ="//input[@type='email']"
        self.login_nextbtn ="//*[@id='identifierNext']/span"
        self.login_pwd ="//input[@name='password']"
        self.login_signbtn ="//input[@id='signIn']"

    def login(self, username ,password):
        self.set_login_email(username)
        self.login_nextbtn()
        self.set_login_pwd(password)
        self.login_signbtn()

        if 'Qxf2 Mail' in self.driver.title:
            self.write("Login success !")
            return  True
        else:
            self.write("login failed !")
            return  False
    def set_login_email(self,username):
        "Set the username on the login screen "

    def submit_next(self):
        self.click_element(self.login_nextbtn)
        self.wait(3)

    def set_login_pwd(self,password):
        "set password on login screen "

    def submit_login(self):
        "submit login form "

