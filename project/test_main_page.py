from project.pages.MainPage import MainPageClass
from project.pages.LoginPage import LoginPageClass
from project.pages.basket_page import BasketPage
import pytest

links = ['http://selenium1py.pythonanywhere.com/']


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    page = MainPageClass(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page(browser, link):
    page = MainPageClass(browser,
                         link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPageClass(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', links)
def test_guest_go_to_basket(browser, link):
    page = MainPageClass(browser, link)
    page.open()
    page.go_to_basket()
    new_page = BasketPage(browser, browser.current_url)
    new_page.should_be_basket()


@pytest.mark.parametrize('link', links)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPageClass(browser, link)
    page.open()
    page.go_to_basket()
    new_page = BasketPage(browser, browser.current_url)
    new_page.is_basket_empty()
