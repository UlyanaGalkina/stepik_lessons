import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class TestLoginPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()

    @pytest.mark.personal_tests
    @pytest.mark.xfail
    @pytest.mark.negative_case
    def test_register_with_invalid_password(self, browser):
        page = LoginPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = login_page.generate_unique_email()
        login_page.register_new_user(email, "123")
        login_page.should_be_authorized_user()