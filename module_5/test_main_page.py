from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty()


    # def test_add_to_cart(browser):
    #     page = ProductPage(url="", browser)  # инициализируем объект Page Object
    #     page.open()  # открываем страницу в браузере
    #     page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    #     page.add_product_to_cart()  # жмем кнопку добавить в корзину
    #     page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом