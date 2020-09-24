import time
from selenium.webdriver.support.select import Select
class AddCustomer:

    lnkCustomer_menu_xpath="//ul[@class='sidebar-menu tree']/li[4]/a/span"
    lnkCustomer_menuitem_xpath="//ul[@class='sidebar-menu tree']/li[4]/ul/li[1]/a"
    btn_AddCustomer_xpath="//a[@href='/Admin/Customer/Create']"

    textEmail_xpath ="//input[@id='Email']"
    textPassword_xpath="//input[@id='Password']"
    textFirstName_xpath = "//input[@id='FirstName']"
    textLastName_xpath = "//input[@id='LastName']"

    radiobtn_Male_xpath="//input[@id='Gender_Male']"
    radiobtn_FeMale_xpath = "//input[@id='Gender_Female']"
    txtbox_DOB_xpath ="//input[@id='DateOfBirth' or @name='DateOfBirth']"

    txtbox_Company_xpath="//input[@name='Company']"
    checkBox_IsTaxExempt_xpath="//input[@id='IsTaxExempt']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    txtNews_xpath ="//div[@class='k-widget k-multiselect k-multiselect-clearable']"


    def __init__(self,driver):
        self.driver=driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()

    def clickonAddCustomerBtn(self):
        self.driver.find_element_by_xpath(self.btn_AddCustomer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.textEmail_xpath).send_keys(email)

    def setPasword(self, password):
        self.driver.find_element_by_xpath(self.textPassword_xpath).send_keys(password)

    def setFirstName(self,firstName):
        self.driver.find_element_by_xpath(self.textFirstName_xpath).send_keys(firstName)

    def setLastName(self,lastName):
        self.driver.find_element_by_xpath(self.textLastName_xpath).send_keys(lastName)

    def setGender(self,gender):

        if gender=="female" or gender=="f" or gender=="Female" :
            self.driver.find_element_by_xpath(self.radiobtn_FeMale_xpath).click()

        else:
            self.driver.find_element_by_xpath(self.radiobtn_Male_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.txtbox_DOB_xpath).send_keys(dob)

    def setCompanyName(self,companyName):
        self.driver.find_element_by_xpath(self.txtbox_Company_xpath).send_keys(companyName)

    def setIstaxexempt(self,value):

        self.org_value= self.driver.find_element_by_xpath(self.checkBox_IsTaxExempt_xpath).is_selected()

        if value==self.org_value :
            self.driver.find_element_by_xpath(self.checkBox_IsTaxExempt_xpath).is_selected()
        else:
            self.driver.find_element_by_xpath(self.checkBox_IsTaxExempt_xpath).click()

    def setManagerofvendor(self,value):
        list= Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        list.select_by_index(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click();
        self.driver.execute_script("arguments[0].click();", self.listitem)







































































