
from helpers.support_functions import find_element_xpath, wait_for_visibility_of_element_id, wait_for_visibility_of_element_xpath

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

checkboxes_tab = '//*[@id="content"]/ul/li[6]/a'
all_checkboxes = 'checkboxes'
checkbox_1 = '//*[@id="checkboxes"]/input[1]'
checkbox_2 = '//*[@id="checkboxes"]/input[2]'


def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, checkboxes_tab)
    elem =driver_instance.find_element(by=By.XPATH, value=checkboxes_tab)  
    elem.click()


def checkboxes_content_visible(driver_instance):
    elem =driver_instance.find_element(by=By.ID, value=all_checkboxes) 
    return elem.is_displayed()

def valaidate_checkbox1(driver_instance):
    elem_1 =driver_instance.find_element(by=By.XPATH, value=checkbox_1).is_selected()
    return elem_1


def valaidate_checkbox2(driver_instance):
    elem_2 =driver_instance.find_element(by=By.XPATH, value=checkbox_2).is_selected()
    return elem_2 


