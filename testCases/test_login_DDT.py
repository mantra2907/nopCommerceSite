import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_DDT_Login:

    baseURL= ReadConfig.getApplicationURl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setupBrowserDriver):


        self.logger.info(" *************** this test case 1 *************** ")
        self.logger.info(" *************** verifing case 1 *************** ")
        self.driver = setupBrowserDriver
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info(" ************************** this test case 1 is pass ************************ ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error(" ************************** this test case 1 is fail ************************ ")
            assert False

    def test_login(self, setupBrowserDriver):

        self.logger.info(" ************************** this test case 2 ************************ ")
        self.driver = setupBrowserDriver
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print("after login page title :: "+act_title)

        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info(" ************************** this test case 2 is pass ************************ ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"afterlogin_page_title.png")
            assert False
            self.logger.error(" ************************** this test case 2 is fail ************************ ")
































