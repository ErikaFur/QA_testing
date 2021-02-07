from project.pages.BasePage import BasePageClass
from project.pages.locators import BasketPageLocators


class BasketPage(BasePageClass):
    def should_be_basket(self):
        assert ('/basket/') in self.browser.current_url, "This page is not basket"

    def is_basket_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is not message that basket is empty"
