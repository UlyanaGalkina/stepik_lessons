from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-group>a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')
    BASKET_SUCCESS_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')

# class BasketPageLocators():
#     EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
#     BASKET_ITEMS_HEADER = (By.CSS_SELECTOR, ".basket-items")
#
# class ProductPageLocators():
#     ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".add-to-basket button")
#     ADDED_PRODUCT_TEXT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
#     BASKET_PRICE_TEXT = (By.CSS_SELECTOR, ".alertinner p strong")
#     PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, ".product_main h1")
#     PRODUCT_PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")

    # REGISTER_EMAIL = "#id_registration-email"
    # REGISTER_PASS = "#id_registration-password1"
    # REGISTER_PROVE_PASS = "#id_registration-password2"
    # REGISTER_BTN = "#register_form > button"
    # REGISTER_MESSAGE = ".alertinner.wicon"
    #  = (By.CSS_SELECTOR, "#id_registration-email")
    #  = (By.CSS_SELECTOR, "#id_registration-password1")
    #  = (By.CSS_SELECTOR, "#id_registration-password2")
    #  = (By.NAME, "registration_submit")

class BasketPageLocators(BasePageLocators):
    BASKET_ALERT = (By.CSS_SELECTOR, '.alertinner')
    BASKET_CONTENT = (By.CSS_SELECTOR, '.content > #content_inner')
    BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BASKET_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(2)')
    BASKET_ORDER_TOTAL = (By.CSS_SELECTOR, '.total > .price_color')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')