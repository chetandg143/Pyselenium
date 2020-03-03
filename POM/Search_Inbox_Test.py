import os

from POM import Page_Factory, Conf_Reader
from POM import DriverFactory
from POM.DriverFactory import driver



def run_search_inbox_test(browser , conf ,base_url ,sauce_flag,browser_version,platform,testrail_run_id):
    credentials_file = os.path.join(os.path.dirname("/home/tibil/PycharmProjects/Selenium/POM/credentials_file"),'login.credentials')
    username = Conf_Reader.get_value(credentials_file,'LOGIN_USER')
    password = Conf_Reader.get_value(credentials_file,'LOGIN_PASSWORD')

#Result flag used by TestRail
    result_flag = False

#Setup a driver
#create object of driver factory
    driver_obj = DriverFactory()
    driver = driver_obj.get_web_driver(browser,sauce_flag,browser_version,platform)
    driver.maximize_window()


#Create a login page object
    login_obj = Page_Factory.get_page_object("login",driver)
    if (login_obj.login(username,password)):
        msg = "Login was successful"
        result_flag = True
        login_obj.write(msg)
    else:
        msg = "Login failed"
        login_obj.write(msg)

#Create an object for main page with header and menu
main_obj = Page_Factory.get_page_object("main",driver)
main_obj.wait(3)

#Search the inbox for message by subject 'POM' and open the message
if main_obj.header_obj.search_by_subject('POM'):
    main_obj.write("Search successful")
    result_flag = True
else:
    main_obj.write("Search text was not found")
    result_flag = False

#Go to inbox
main_obj.menu_obj.select_menu_item('inbox')