# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys("admin")
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys("secret")
        driver.find_element(By.XPATH, "//input[@value='Login']").click()
        driver.find_element(By.LINK_TEXT, "groups").click()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys("Faggot")
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys("YOU")
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys("YOOOOUUUU")
        driver.find_element(By.NAME, "submit").click()
        driver.find_element(By.LINK_TEXT, "groups").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
