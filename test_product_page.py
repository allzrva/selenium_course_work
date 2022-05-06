"""
Runs tests from Module 4.3 https://stepik.org/lesson/201964/?unit=176022
Tests to be run with command 'pytest -v -s --tb=line --language=en test_product_page.py'
"""
import pytest

from pages.product_page import ProductPage

# For Task 4.3.2 use the link below and 'test_guest_can_add_product_to_basket'.
# Comment all other link options, remove @pytest.mark.skip fixture.
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

# For task 4.3.3 use the link below and 'test_guest_can_add_product_to_basket'.
# Comment all other link options, remove @pytest.mark.skip fixture.
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
"""
For task 4.3.4:
- use the link below
source_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
- remove @pytest.mark.skip fixture from 'test_guest_can_add_product_to_basket'
- add pytext.mark.parametrize fixture right before the 'test_guest_can_add_product_to_basket'
@pytest.mark.parametrize('link', [f'{source_link}?promo=offer{i}' if i != 7
                                  else pytest.param(f'{source_link}?promo=offer{i}', marks=pytest.mark.xfail)
                                  for i in range(10)])
- add additional input parameter 'link' from parametrize fixture
test_guest_can_add_product_to_basket(browser, link)
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_cart_link()
    page.solve_quiz_and_get_code()
    page.verify_correct_product_name_in_cart()
    page.verify_correct_product_price_in_cart()

# region task 4_3_6


"""
lessons available at https://stepik.org/lesson/201964/step/5?unit=176022 and https://stepik.org/lesson/201964/step/6?unit=176022
link for the test web page should be link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
All tests in the region are skipped because the task was temporary
"""


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_cart_link()
    page.verify_no_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.verify_no_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_cart_link()
    page.verify_message_disappeared()

# endregion task 4_3_6
