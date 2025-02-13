from settings import *
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    LOGIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/accounts/login/"

    def __init__(self, driver, url=LOGIN_PAGE_URL):
        super().__init__(driver, url)
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.driver.current_url, "Substring 'login' is not present in the current URL"

    def register_new_user(self, email, password):
        reg_email = self.driver.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        print('Your email:', email)
        reg_password = self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        reg_password_confirm = self.driver.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        print('Your password:', password)
        reg_btn = self.driver.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"