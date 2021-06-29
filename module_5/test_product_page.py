from .pages.product_page import ProductPage
import pytest

class TestProductPage():
    # @pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    # def test_guest_can_add_product_to_basket(self, browser, promo_offer):
    #     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #     promo_link = '?promo='
    #     item_page = ProductPage(browser, link + promo_link + promo_offer)
    #     item_page.open()
    #     item_page.add_to_basket()
    #     item_page.solve_quiz_and_get_code()

# class TestProductPage():
#     def test_guest_can_add_product_to_basket(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#         item_page = ProductPage(browser, link)
#         item_page.open()
#         item_page.add_to_basket()
#         item_page.solve_quiz_and_get_code()
#         item_page.check_item_name()
#         item_page.check_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_dissapeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_dissapear_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(self, browser, browser.current_url)
        basket_page.check_basket_empty_message()
        basket_page.check_basket_not_have_checkout()