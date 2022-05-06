"""
run test with command pytest -v -s --tb=line --language=en test_product_page.py
test corresponds to task
"""
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_cart_link()
    page.solve_quiz_and_get_code()
    page.verify_correct_product_name_in_cart()
    page.verify_correct_product_price_in_cart()
