import datetime

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    login_page_url = "/login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.login_page_url in self.browser.current_url, \
            self.login_page_url + " is not present in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented on page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented on page"

    def generate_unique_email(self):
        uniq = int(datetime.datetime.now().timestamp())
        return "namaste+" + str(uniq) + "@test.test"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        submit_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        pass_input.send_keys(password)
        confirm_input.send_keys(password)
        submit_btn.click()
