from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Page Object for the basket page of the web site
    """
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def verify_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            f"Basket should be empty, but some elements are found: {self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)}"

    def verify_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            f"No text element with locator {BasketPageLocators.BASKET_EMPTY_TEXT.value}"
