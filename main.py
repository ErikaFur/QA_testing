from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
import unittest

class TestWeb(unittest.TestCase):
    def test_web1(self):
        link = "http://suninjuly.github.io/registration1.html"
        data = {"first":"aboba", "second":"Dirova", "third":"aboba@mail.com"}
        browser = webdriver.Chrome()
        browser.get(link)

        required = browser.find_elements_by_css_selector('input[required]')
        for i in required:
            a = i.get_attribute("class").split()[-1]
            send_data = data[a]
            self.assertNotEqual(send_data.__len__(), 0, f"{a} input should not be empty")
            if a == "third":
                self.assertIn("@", send_data, f"Mail should be correct, but got {send_data}")
            i.send_keys(data[a])

        button = browser.find_element_by_css_selector('button[type="submit"]')
        button.click()

        answer = browser.find_element_by_class_name("container").text
        browser.quit()
        self.assertEqual(answer, "Congratulations! You have successfully registered!", "Something was wrong :(")

    def test_web2(self):
        link = "http://suninjuly.github.io/registration2.html"
        data = {"first":"aboba", "second":"Dirova", "third":"aboba@mail.com"}
        browser = webdriver.Chrome()
        browser.get(link)

        required = browser.find_elements_by_css_selector('input[required]')
        for i in required:
            a = i.get_attribute("class").split()[-1]
            send_data = data[a]
            self.assertNotEqual(send_data.__len__(), 0, f"{a} input should not be empty")
            if a == "third":
                self.assertIn("@", send_data, f"Mail should be correct, but got {send_data}")
            i.send_keys(data[a])

        button = browser.find_element_by_css_selector('button[type="submit"]')
        button.click()

        answer = browser.find_element_by_class_name("container").text
        browser.quit()
        self.assertEqual(answer, "Congratulations! You have successfully registered!", "Something was wrong :(")

unittest.main()

