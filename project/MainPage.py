from project.BasePage import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from project.locators import MainPageLocators
from project.LoginPage import LoginPageClass


class MainPageClass(BasePageClass):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPageClass(browser = self.browser, url = self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


    def go_to_basket(self):
        basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True