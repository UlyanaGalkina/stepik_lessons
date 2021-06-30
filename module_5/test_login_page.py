from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class TestLoginPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()