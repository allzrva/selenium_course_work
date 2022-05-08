from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Page Object for the product page of the web site.
    All methods cover 'Add to basket' scenario, but verify content present on the product page only
    """
    def click_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket element is absent"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def verify_product_name_added_to_basket(self):
        try:
            assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_BASKET), \
                "Name of the product is absent in the response banner"
        finally:
            banner_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            assert banner_name == product_name,\
                f"Name of the product in the banner '{banner_name}' does not correspond " \
                f"to the expected product name '{product_name}'."

    def verify_product_price_added_to_basket(self):
        try:
            assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_BASKET), \
                "Basket total is absent in the response banner"
        finally:
            banner_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
            product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
            assert banner_price == product_price, \
                f"Price of the product in the banner '{banner_price}' does not correspond " \
                f"to the expected product name '{product_price}'"

    def verify_no_success_message(self):
        # Success message = message when the product has been successfully added to cart
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message about successful addition to basket is present, but should not be"

    def verify_message_disappeared(self):
        # Success message = message when the product has been successfully added to cart
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message about successful addition to basket should disappear in no longer than 4 seconds"
