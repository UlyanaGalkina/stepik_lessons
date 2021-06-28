from .pages.product_page import ProductPage

class TestProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.add_to_basket()
        item_page.solve_quiz_and_get_code()
        item_page.check_item_name()
        item_page.check_price()