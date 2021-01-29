from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR,'*.btn[href="/ru/basket/"]')


class LoginPageLocator():
    REGISTRATION_FIELD = (By.ID, "register_form")
    LOGIN_FIELD = (By.ID, "login_form")

class ObjectPageLocator():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_CONFIRMATION = (By.CSS_SELECTOR, 'div.alertinner strong')
    NAME_OF_GOOD = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    GOOD_PRICE = (By.CSS_SELECTOR, 'p.price_color')