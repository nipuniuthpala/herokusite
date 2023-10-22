import unittest

from selenium import webdriver
from page_objects import upload_confirmation_page, file_upload_page, checkboxes_page, main_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://the-internet.herokuapp.com/'
        self.driver.get(self.url)
        self.driver.maximize_window()


    # Main Page Test
    def test_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))
       
   
   
    # Checkboxes Page Test
    def test_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_content_visible(self.driver))
        self.assertFalse(checkboxes_page.valaidate_checkbox1(self.driver))
        self.assertTrue(checkboxes_page.valaidate_checkbox2(self.driver))
       
   
   
    # Upload File Page Tests
    def test_upload_file(self):
        file_upload_page.click_file_upload_tab(self.driver)
        self.assertTrue(file_upload_page.file_upload_content_visible(self.driver))
        file_upload_page.choose_file(self.driver)
        upload_confirmation_page.file_uploaded_msg_visible(self.driver)

   
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
