from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR,'*.btn[href="/ru/basket/"]')


class LoginPageLocator():
    REGISTRATION_FIELD = (By.ID, "register_form")
    LOGIN_FIELD = (By.ID, "login_form")