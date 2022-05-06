from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "Add to cart element is absent"
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN).click()

    def verify_correct_product_name_in_cart(self):
        try:
            assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_CART), \
                "Name of the product is absent in the response banner"
        finally:
            banner_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART).text
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            assert banner_name == product_name,\
                f"Name of the product in the banner '{banner_name}' does not correspond " \
                f"to the expected product name '{product_name}'."

    def verify_correct_product_price_in_cart(self):
        try:
            assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_CART), \
                "Basket total is absent in the response banner"
        finally:
            banner_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART).text
            product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
            assert banner_price == product_price, \
                f"Price of the product in the banner '{banner_price}' does not correspond " \
                f"to the expected product name '{product_price}'"
