import pytest
from project.MainPage import MainPageClass
from project.LoginPage import LoginPageClass
from project.ObjectPage import ObjectPageClass
from project.basket_page import BasketPage
from project.locators import ObjectPageLocator


links = ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"]

@pytest.mark.xfail(reason="there is no BASKET")
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ObjectPageClass(browser, link)
    page.open()
    page.add_to_basket()
    page.check_was_added()

@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="there is no such function")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ObjectPageClass(browser, link)
    page.open()
    page.add_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ObjectPageClass(browser, link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="there is no such function")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ObjectPageClass(browser, link)
    page.open()
    page.add_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link_on_product_page(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ObjectPageClass(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ObjectPageClass(browser, link)
    page.open()
    page.go_to_login_page()
    new_page = LoginPageClass(browser, browser.current_url)
    new_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPageClass(browser, link)
    page.open()
    page.go_to_basket()
    new_page = BasketPage(browser, browser.current_url)
    new_page.is_basket_empty()
