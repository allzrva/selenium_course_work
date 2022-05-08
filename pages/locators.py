"""
Page Object with constants for common web page selectors
"""
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_USER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BTN = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert > div > p> strong")


class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
