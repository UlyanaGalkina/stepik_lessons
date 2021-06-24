
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")

def test_ukraine_language(browser):
    expected = "Додати в кошик"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert browser.find_element(*BUTTON_ADD_TO_BASKET)
    assert actual == expected, f"{actual} != {expected} in Ukraine language"

def test_russian_language(browser):
    expected = "Добавить в корзину"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert browser.find_element(*BUTTON_ADD_TO_BASKET)
    assert actual == expected, f"{actual} != {expected} in Russian language"

def test_english_language(browser):
    expected = "Add to basket"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert browser.find_element(*BUTTON_ADD_TO_BASKET)
    assert actual == expected, f"{actual} != {expected} in English language"

def test_spanish_language(browser):
    expected = "Añadir al carrito"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert browser.find_element(*BUTTON_ADD_TO_BASKET)
    assert actual == expected, f"{actual} != {expected} in Spanish language"

def test_france_language(browser):
    expected = "Ajouter au panier"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert browser.find_element(*BUTTON_ADD_TO_BASKET)
    assert actual == expected, f"{actual} != {expected} in France language"