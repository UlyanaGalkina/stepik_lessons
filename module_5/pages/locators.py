from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_EMAIL = "#id_login-username"
    LOGIN_PASSWORD = "#id_login-password"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # REGISTER_EMAIL = "#id_registration-email"
    # REGISTER_PASS = "#id_registration-password1"
    # REGISTER_PROVE_PASS = "#id_registration-password2"
    # REGISTER_BTN = "#register_form > button"
    # REGISTER_MESSAGE = ".alertinner.wicon"
    #  = (By.CSS_SELECTOR, "#id_registration-email")
    #  = (By.CSS_SELECTOR, "#id_registration-password1")
    #  = (By.CSS_SELECTOR, "#id_registration-password2")
    #  = (By.NAME, "registration_submit")