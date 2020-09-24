import random
import string
from pageObjects.CreateCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_AddCustomer:

    baseURL= ReadConfig.getApplicationURl()
    userName= ReadConfig.getUseremail()
    userPassword =ReadConfig.getPassword()
    logger= LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Validate_addCustomer(self,setupBrowserDriver):
        self.logger.info("********* testcase 3 login*************")
        self.driver=setupBrowserDriver
        self.driver.get(self.baseURL)
        self.logger.info("********* login *************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.userPassword)
        self.lp.clickLogin()
        self.logger.info("****************** Admin Logged In *************************")
        self.ac = AddCustomer(self.driver)
        self.driver.maximize_window()
        self.ac.clickonCustomerMenu()
        self.ac.clickonCustomerMenuItem()
        self.ac.clickonAddCustomerBtn()

# Enter Emailid first randomly we create a id and merge with gmail.com

        self.emailid=random_generator()+'@gmail.com'
        self.ac.setEmail(self.emailid)
        self.ac.setPasword("abc123")
        self.ac.setFirstName("sam")
        self.ac.setLastName("Billing")
        self.ac.setGender("female")
        self.ac.setDOB("12-11-2000")
        self.ac.setCompanyName("company")
        self.ac.setIstaxexempt("true")
        self.ac.setManagerofvendor(1)
        print("list vendor ")
        self.ac.setAdminContent("admin content")
        self.ac.clickOnSave()

        self.msg=self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text

        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("**************** customer has been added successfully. ***************")
            self.driver.close()
        else:
            assert True==False
            self.logger.critical("**************** customer has been not added successfully. ***************")
            self.driver.close()

    @pytest.mark.regression
    def test_Validate_Failing_addCustomer(self, setupBrowserDriver):
        self.logger.info("********* testcase 4 login*************")
        self.driver = setupBrowserDriver
        self.driver.get(self.baseURL)
        self.logger.info("********* login *************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.userPassword)
        self.lp.clickLogin()
        self.logger.info("****************** Admin Logged In *************************")
        self.ac = AddCustomer(self.driver)
        self.driver.maximize_window()
        self.ac.clickonCustomerMenu()
        self.ac.clickonCustomerMenuItem()
        self.ac.clickonAddCustomerBtn()
        self.ac.clickOnSave()
        self.logger.info("************ without entering register info click on save")

        self.msg=self.driver.find_element_by_xpath("//div[@class='alert alert-danger alert-dismissable']").text
        print("print ing msge  ::: ",self.msg)

        if "Valid Email is required for customer to be in 'Registered' role" in self.msg:
            assert True== True
            self.logger.info("*********** testcase pass when no info entered and not saving customer ************* ")
            self.driver.close()
        else:
            assert True==False
            self.logger.info("*********** testCase Failed when no info entered and saving customer ************* ")
            self.driver.close()









def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
















