from helpers.support_functions import find_element_by_id, wait_for_visibility_of_element_xpath
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

header = '//*[@id="content"]/ul/li[18]/a'
content = 'content'
choose_file_button = 'file-upload'
upload_button = 'file-submit'


def click_file_upload_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, header)
    elem =driver_instance.find_element(by=By.XPATH, value=header)  
    elem.click()


def file_upload_content_visible(driver_instance):
    elem =driver_instance.find_element(by=By.ID, value=content) 
    return elem.is_displayed()


def choose_file(driver_instance):
    elem_1 =driver_instance.find_element(by=By.ID, value=choose_file_button) 
    elem_1.send_keys('/Users/nipuni/Downloads/herokusite/attachement.pdf')
    elem_2 = find_element_by_id(driver_instance,upload_button)
    elem_2.click()
