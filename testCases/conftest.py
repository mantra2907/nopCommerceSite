from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver= webdriver.Chrome()
    #driver.find_element_by_class_name()
    #driver.find_element_by_xpath()
    return driver