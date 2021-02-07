from project.pages.BasePage import BasePageClass
from project.pages.locators import LoginPageLocator


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


    def register_new_user(self, email, password):
        self.should_be_login_page()
        assert "@" in email, "Incorrect email"
        assert "." in email, "Incorrect email"
        assert email.rfind('.') >  email.index('@') + 1,  "Incorrect email"
        assert password.__len__() >= 9, "Incorrect password"
        email_field = self.browser.find_element(*LoginPageLocator.REG_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocator.REG_PASSWORD_FIELD_1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocator.REG_PASSWORD_FIELD_2)
        password_field2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocator.REG_BUTTON)
        button.click()
        assert self.is_element_present(*(LoginPageLocator.REG_SUCCESS)), "Registration was not successed"



