from Prpom.Driver import drivers

from Prpom import frameadd
class logindetails:
    drivers.find_element_by_name("email").send_keys("@gmail.com")
    drivers.find_element_by_id("continue").click()
    drivers.find_element_by_name("password").send_keys("*******")
    drivers.find_element_by_id("signInSubmit").click()