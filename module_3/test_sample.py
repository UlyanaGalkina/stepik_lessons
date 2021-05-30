from selenium import webdriver
import random

main_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

registration_email_input_locator = "#id_registration-email"
registration_password_input_locator = "#id_registration-password1"
registration_repeat_password_input_locator = "#id_registration-password2"
registration_button_locator = "#register_form > button"
registration_thank_message_locator = ".alertinner.wicon"


def test_registration_with_valid_data():
    # Data
    registration_random_email = str(random.randint (10,100000000000000)) + "@test.test"
    registration_password = random.randint (999999999,100000000000000)
    thank_for_registration_text = "Спасибо за регистрацию!"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        registration_email_input = browser.find_element_by_css_selector(registration_email_input_locator)
        registration_password_input = browser.find_element_by_css_selector(registration_password_input_locator)
        registration_repeat_password_input = browser.find_element_by_css_selector(registration_repeat_password_input_locator)


        # Act
        registration_email_input.send_keys(registration_random_email)
        registration_password_input.send_keys(registration_password)
        registration_repeat_password_input.send_keys(registration_password)

        browser.find_element_by_css_selector(registration_button_locator).click()

        print("email -", registration_random_email, "password -", registration_password)

        # Assert
        registration_thank_message_text = browser.find_element_by_css_selector(registration_thank_message_locator)
        recieved_registration_thank_text = registration_thank_message_text.text
        assert thank_for_registration_text in recieved_registration_thank_text, f"Page should contain {thank_for_registration_text} now contain {recieved_registration_thank_text} "

    finally:
        browser.quit()

test_registration_with_valid_data()