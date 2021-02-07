from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocator():
    REGISTRATION_FIELD = (By.ID, "register_form")
    LOGIN_FIELD = (By.ID, "login_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, 'input[id$="email"]')
    REG_PASSWORD_FIELD_1 = (By.CSS_SELECTOR, 'input[id$="password1"]')
    REG_PASSWORD_FIELD_2 = (By.CSS_SELECTOR, 'input[id$="password2"]')
    REG_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REG_SUCCESS = (By.CSS_SELECTOR, 'div.alert-success')

class ObjectPageLocator():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_CONFIRMATION = (By.CSS_SELECTOR, 'div.alertinner strong')
    NAME_OF_GOOD = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    GOOD_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:first-child')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'a.btn[href$="/basket/"]:first-child')
    USER_ICON = (By.CSS_SELECTOR, 'a[href$="/accounts/"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')
