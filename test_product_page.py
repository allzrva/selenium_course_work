"""
run test with command pytest -v -s --tb=line --language=en test_product_page.py
test corresponds to task
"""
import pytest

from pages.product_page import ProductPage

# link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" link for 4_3_2 task
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" link for 4_3_3 task
source_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"  # link for 4_3_4 task


@pytest.mark.parametrize('link', [f'{source_link}?promo=offer{i}' if i != 7
                                  else pytest.param(f'{source_link}?promo=offer{i}', marks=pytest.mark.xfail)
                                  for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_cart_link()
    page.solve_quiz_and_get_code()
    page.verify_correct_product_name_in_cart()
    page.verify_correct_product_price_in_cart()
