import time

from project.BasePage import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from project.basket_page import BasketPage
from project.locators import MainPageLocators
from project.LoginPage import LoginPageClass
from project.locators import ObjectPageLocator


class ObjectPageClass(BasePageClass):

    def add_to_basket(self):
        assert self.is_element_present(*ObjectPageLocator.BASKET_BUTTON), "There is not basket button"
        basket = self.browser.find_element(*ObjectPageLocator.BASKET_BUTTON)
        #assert "disable" in basket.get_attribute('class'), "Basket button is disabled"
        basket.click()

    def add_to_basket_with_quiz(self):
        assert self.is_element_present(*ObjectPageLocator.BASKET_BUTTON), "There is not basket button"
        basket = self.browser.find_element(*ObjectPageLocator.BASKET_BUTTON)
        # assert "disable" in basket.get_attribute('class'), "Basket button is disabled"
        basket.click()
        self.solve_quiz_and_get_code()

    def check_was_added(self):
        assert self.is_element_present(*ObjectPageLocator.NAME_CONFIRMATION), "There is not confirmation about adding good to the basket"

        name_in_notification = self.browser.find_elements(*ObjectPageLocator.NAME_CONFIRMATION)[0].text
        name = self.browser.find_element(*ObjectPageLocator.NAME_OF_GOOD).text
        assert name_in_notification == name , f"Names of good in notification should be {name}, but got {name_in_notification}"

        price_in_basket = self.browser.find_element(*ObjectPageLocator.BASKET_PRICE).text
        price_of_good = self.browser.find_element(*ObjectPageLocator.GOOD_PRICE).text
        assert price_of_good == price_in_basket, f"Price of basket is {price_in_basket} and good's is {price_of_good}, but should be equal"

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ObjectPageClass(browser, link)
        page.open()
        page.go_to_basket()
        new_page = BasketPage(browser, browser.current_url)
        new_page.is_basket_empty()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ObjectPageLocator.SUCCESS_MESSAGE),  "Object is presented!"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ObjectPageLocator.SUCCESS_MESSAGE), "Object is not disapeared"