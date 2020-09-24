from pageObjects.searchCustomerPage import SearchCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateCustomer import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import pdb
class Test_SearchCustomerBy:

    baseURL=ReadConfig.getApplicationURl()
    userName=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    def loginPage(self,setupBrowserDriver):
        self.logger.info("*********launching browser*******")
        self.driver = setupBrowserDriver
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Logged In in lloo *******")
        #return self.driver

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SearchByEmailid(self,setupBrowserDriver):

        self.driver = setupBrowserDriver
        self.login=Test_SearchCustomerBy()
        self.login.loginPage(setupBrowserDriver)

        self.addCust=AddCustomer(self.driver)
        self.addCust.clickonCustomerMenu()
        self.addCust.clickonCustomerMenuItem()
        self.logger.info("********* search by email *******")

        self.searchcust=SearchCustomerPage(self.driver)
        self.searchcust.searchByEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.searchByNOCustomerRole()
        self.searchcust.clickOnSearch()
        self.flag=self.searchcust.verifysearchEmailverify("victoria_victoria@nopCommerce.com")
        if self.flag== True:
            self.logger.info("*************** search by email pass ***********************")
            self.driver.close()
        else:
            self.logger.info("************* search by email fail ******")
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SearchByCustomerRole(self, setupBrowserDriver):
        self.driver = setupBrowserDriver
        self.login = Test_SearchCustomerBy()
        self.login.loginPage(setupBrowserDriver)

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickonCustomerMenu()
        self.addCust.clickonCustomerMenuItem()
        self.logger.info("********* search by customer role *******")
        #pdb.set_trace()
        self.searchcust = SearchCustomerPage(self.driver)
        #self.searchcust.searchByNOCustomerRole()
        #self.searchcust.searchByCustomerRole("Registered")
        self.searchcust.clickOnSearch()
        self.flag=self.searchcust.verifyCustomeRolesearch("Registered")
        if self.flag== True:
            self.logger.info("*************** customer role search pass ***********************")
            self.driver.close()
        else:
            self.logger.info("*************customer role search fail ******")
            self.driver.close()


