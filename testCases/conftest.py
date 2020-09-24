from selenium import webdriver
import pytest

@pytest.fixture()
def setupBrowserDriver(browser):
    if browser=='Ie':
        driver= webdriver.Ie()
    elif browser=='firefox':
        driver= webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

################ pytest HTML Report #####################

#It is hook for adding Envioroment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']="Account"
    config._metadata['Tester'] ="Saurabh"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

















