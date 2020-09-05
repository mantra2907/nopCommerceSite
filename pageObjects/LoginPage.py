from selenium import webdriver

class LoginPage:

    text_username_id="Email"
    text_password_id="Password"
    button_login_xpath="//input[@class='button-1 login-button']"
    #button_login_class ="button-1 login-button"
    link_loogout_xpath="//a[text()='Logout']"

    #intial driver
    def __init__(self, driver):
        #python contructur automatio=al invoke while object create
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_password_id).clear()
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


    def clickLogOut(self):
        self.driver.find_element_by_xpath(self.link_loogout_xpath).click()
























