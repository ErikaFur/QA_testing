import time
import pytest
from project.pages.MainPage import MainPageClass
from project.pages.LoginPage import LoginPageClass
from project.pages.ObjectPage import ObjectPageClass
from project.pages.basket_page import BasketPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ObjectPageClass(browser, link)
    page.open()
    page.add_to_basket()
    page.check_was_added()


@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="there is no such function")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ObjectPageClass(browser, link)
    page.open()
    page.add_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ObjectPageClass(browser, link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="there is no such function")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ObjectPageClass(browser, link)
    page.open()
    page.add_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ObjectPageClass(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ObjectPageClass(browser, link)
    page.open()
    page.go_to_login_page()
    new_page = LoginPageClass(browser, browser.current_url)
    new_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPageClass(browser, link)
    page.open()
    page.go_to_basket()
    new_page = BasketPage(browser, browser.current_url)
    new_page.is_basket_empty()


@pytest.mark.user_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page_login = LoginPageClass(browser, link)
        page_login.open()
        email = str(time.time()) + "@fakemail.org"
        page_login.register_new_user(email, "pythonanywhere")
        page_login.should_be_authorized_user()

    @pytest.mark.parametrize('link', links)
    def test_user_cant_see_success_message(self, browser, link):
        page = ObjectPageClass(browser, link)
        page.open()
        page.guest_cant_see_success_message_after_adding_product_to_basket()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links)
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ObjectPageClass(browser, link)
        page.open()
        page.add_to_basket()
        page.check_was_added()
