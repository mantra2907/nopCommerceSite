import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL ="https://admin-demo.nopcommerce.com/login"
    username ="admin@yourstore.com"
    password ="admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title =="Your store. Logins":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print("after login page title :: "+act_title)

        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
































