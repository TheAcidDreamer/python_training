# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group

class AddNewGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_group(self):
        wd = self.wd
        self.open_website(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups(wd)
        self.create_new_group(wd, Group(name="Faggot", header="YOU", footer="YOOOOUUUU"))
        self.return_to_groups(wd)
        self.logout(wd)

    def test_empty_group(self):
        wd = self.wd
        self.open_website(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups(wd)
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups(wd)
        self.logout(wd)

    def logout(self, wd):
        # Выход из браузера
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups(self, wd):
        # Возвращение на страницу groups
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_new_group(self, wd, group):
        # Создание новой группы
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()

    def open_groups(self, wd):
        # Открытие страницы groups
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd, username, password):
        # Login
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_website(self, wd):
        # Открываем сайт локал\адресбук
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

# bfd9b11