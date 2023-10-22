from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def wait_for_visibility_of_element_xpath(driver_instance, xpath):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_id(driver_instance, id):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element_xpath(inv_driver_instance, xpath):
    inv_element = WebDriverWait(inv_driver_instance, 8).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_element


def find_element_xpath(inv_driver_instance, xpath):
    inv_element = WebDriverWait(inv_driver_instance, 8).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_element

def find_element_by_id(driver_instance, id):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem