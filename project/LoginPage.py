from project.BasePage import BasePageClass
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from project.locators import LoginPageLocator


class LoginPageClass(BasePageClass):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "accounts/login/" in self.browser.current_url, "URL not from login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocator.LOGIN_FIELD), "On login page is absent login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocator.REGISTRATION_FIELD), "On login page is absent registration form"

