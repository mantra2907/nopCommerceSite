from selenium.webdriver.support.select import Select
from utilities.customLogger import LogGen

class SearchCustomerPage:
    logger=LogGen.loggen()

    txtEmail_xpath="//input[@id='SearchEmail']"
    txtFirstName_xpath="//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    selectDobMonth_xpath="//select[@id='SearchMonthOfBirth']"
    selectDobDay_xpath="//select[@id='SearchDayOfBirth']"
    txtCompany_xpath="//input[@id='SearchCompany']"
    txtIpAddress_xpath="//input[@id='SearchIpAddress']"

    lstCustomerRole_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']"
    lstCustomerRoleAdminstrator_xpath="//li[contains(text(),'Administrators')]"
    lstCustomerRoleForum_xpath="//li[contains(text(),'Forum Moderators')]"
    lstCustomerRoleGuests_xpath ="//li[contains(text(),'Guests')]"
    lstCustomerRoleRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstCustomerRoleVendors_xpath="//li[contains(text(),'Vendors')]"

    table_xpath="//table[@id='customers-grid']"
    tableRow_xpath="//table[@id='customers-grid']/tbody/tr"
    tableColumn_xpath="//table[@id='customers-grid']/tbody/tr/td"
    btnSearch_xpath="//button[@id='search-customers']"

    def __init__(self,driver):
        self.driver=driver

    def searchByEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def searchByFirstName(self,firstName):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstName)

    def searchByLastName(self,lastName):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastName)

    def searchByDob_Day(self,day):
        self.driver.find_element_by_xpath(self.selectDobDay_xpath).send_keys(day)

    def searchByDob_Month(self,month):
        self.driver.find_element_by_xpath(self.selectDobMonth_xpath).send_keys(month)

    def searchByCompany(self,company):
        self.driver.find_element_by_xpath(self.txtCompany_xpath).send_keys(company)

    def searchByIpAddress(self, ipaddress):
        self.driver.find_element_by_xpath(self.txtIpAddress_xpath).send_keys(ipaddress)

    def searchByCustomerRole(self, role):
        lst=Select(self.driver.find_element_by_xpath(self.lstCustomerRole_xpath))
        lst.select_by_visible_text(role)
        '''
        lst = self.driver.find_element_by_xpath(self.lstCustomerRole_xpath)
        items = lst.find_elements_by_tag_name("li")
        for i in items:
            #print(i.get_attribute("innerHTML"))
            if i.get_attribute("innerHTML") == "Administrators":
                self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()
            elif i.get_attribute("innerHTML") == "Forum Moderators":
                self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()
            elif i.get_attribute("innerHTML") == "Guests":
                self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()
            elif i.get_attribute("innerHTML") == "Registered":
                self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()
            elif i.get_attribute("innerHTML") == "Vendors":
                self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()
'''

    def noOfRows(self):
        num_rows = len(self.driver.find_elements_by_xpath(self.tableRow_xpath))
        return num_rows

    def noOfColumn(self):

        return len(self.driver.find_element_by_xpath(self.tableColumn_xpath))



    def verifysearchEmailverify(self,email):
        flag= False
        for i in range(1, self.noOfRows()+1):
            xpath1= "//table[@id='customers-grid']/tbody/tr"+str([i])+"/td[2]"
            print("print created xpath :: ",xpath1)
            emailid=self.driver.find_element_by_xpath(xpath1).text

            if emailid== email:
                print("matched", emailid)
                flag= True
            elif email in emailid:
                print("matched", emailid)
                flag = True
            else:
                print("Not matched", emailid)
                break
        return flag

    def verifyCustomeRolesearch(self, role):
        flag = False
        count=0
        for i in range(1, self.noOfRows() + 1):
            xpath1 = "//table[@id='customers-grid']/tbody/tr[" + str(i) + "]/td[4]"
            print("print created xpath :: ", xpath1)
            role_tables = self.driver.find_element_by_xpath(xpath1).text

            if role_tables == role:
                print("matched", role_tables)
                count=count+1
                flag = True
            elif role in role_tables:
                count=count+1
                flag=True
            else:
                print("Not matched", role_tables)
                break
        print("total no of count:: ", count)
        return flag



    def searchByNOCustomerRole(self):

        self.driver.find_element_by_xpath(self.lstCustomerRole_xpath)
        self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()

    def clickOnSearch(self):
        print("search button")
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()



