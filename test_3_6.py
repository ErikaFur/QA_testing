from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
import pytest
import unittest


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class Test_3_6:

    @pytest.fixture(scope="session")
    def browser_init(self):
        browser = webdriver.Chrome()
        yield browser
        browser.quit()

    def test_web_3_6(self, browser_init, links):
        link = f"{links}"
        browser_init.get(link)

        time.sleep(3)
        input_row = browser_init.find_element_by_css_selector('textarea.textarea')
        input_row.send_keys(str(math.log(int(time.time()))))
        button = browser_init.find_element_by_css_selector('button[class="submit-submission"]')
        button.click()

        time.sleep(2)
        answer = browser_init.find_element_by_css_selector('pre.smart-hints__hint').text

        assert answer == "Correct!", print(f"Got answer {answer}, but should be 'Correct!'")
