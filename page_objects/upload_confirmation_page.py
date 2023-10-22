from helpers.support_functions import find_element_xpath, wait_for_visibility_of_element_xpath
from selenium.webdriver.common.by import By


message = '//*[@id="content"]/div/h3'


def file_uploaded_msg_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, message)
    elem =driver_instance.find_element(by=By.XPATH, value=message)  
    return elem.is_displayed()