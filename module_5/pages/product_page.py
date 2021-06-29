from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
# from selenium.webdriver.common.by import
# By from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False


    def get_product_name(self):
        try:
            return str(self.browser.find_element(*ProductPageLocators.ITEM_NAME).text)
        except NoSuchElementException:
            return None

    def get_price(self):
        try:
             return str(self.browser.find_element(*ProductPageLocators.PRICE).text)
        except NoSuchElementException:
             return None


    def check_item_name(self):
        result = self.get_success_message_after_add_product_to_basket()
        product = self.get_product_name()
        assert result == product, 'Product name are not same'

    def get_success_message_after_add_product_to_basket(self):
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))
        try:
            return str(self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        except NoSuchElementException:
            return None



    def get_price_from_message(self):
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(ProductPageLocators.PRICE_MESSAGE))
        try:
            return str(self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text)
        except NoSuchElementException:
            return None

    def check_price(self):
        price = self.get_price()
        price_message = self.get_price_from_message()
        assert price == price_message, 'Price are not same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_SUCCESS_ALERT), \
            'Success message is presented, but should not be'

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_SUCCESS_ALERT), \
            'Success message was presented, but dissapeared'