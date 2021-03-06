import re

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def __parse_price(self, where):
        price_text = self.browser.find_element(*where).text
        search_result = re.search(r"\d+.?\d*", price_text)
        return float(search_result.group(0))

    def add_to_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        price = self.__parse_price(ProductPageLocators.PRODUCT_PRICE)
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()
        return (name, price)

    def check_product_to_basket_confirmed(self, name):
        assert self.is_text_present_at(ProductPageLocators.URGENT_SUCCESS_MESSAGES, f"^{name}$"), \
          f"Отсутсвует подтверждение добавления в корзину, содержащее название продукта ({name})"

    def check_basket_cost(self, expected_cost):
        assert self.is_element_present(*ProductPageLocators.BASKET_MINI), \
            "Текущая цена корзины не найдена"
        cost = self.__parse_price(ProductPageLocators.PRODUCT_PRICE)
        assert cost == expected_cost, \
            f"Неожиданная стоимость корзины {cost}, ожидается {expected_cost}"

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
          "Success message is presented, but should not be"

    def should_success_message_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
          "Success message is presented, but should not be"
