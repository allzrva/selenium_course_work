"""
Runs tests from Module 4.3 https://stepik.org/lesson/201964/?unit=176022
Tests can be run with command 'pytest -v -s --language=en test_product_page.py'
"""
from datetime import datetime
import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """
    Test from the task 4_3_2. Test is expected to pass.
    Replace link with "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" to run task 4_3_3.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.verify_product_name_added_to_basket()
    page.verify_product_price_added_to_basket()


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


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Test from the task 4_3_6. Test is expected to fail. No need in the review for this test, hence skipped.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_basket_button()
    page.verify_no_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    """
    Test from the task 4_3_6. Test is expected to pass. No need in the review for this test, hence skipped.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.verify_no_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Test from the task 4_3_6. Test is expected to fail. No need in the review for this test, hence skipped.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, timeout=5)
    page.open()
    page.click_add_to_basket_button()
    page.verify_message_disappeared()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    """
    Test from the task 4_3_8. Test is expected to pass. No need in the review for this test, hence skipped.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Test from the task 4_3_8. Test is expected to pass.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Test from the task 4_3_10. Test is expected to pass
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.verify_no_items_in_basket()
    basket_page.verify_text_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    """
    Tests from the task 4_3_14. Tests are expected to pass
    """
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link, timeout=5)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        user_email = datetime.now().strftime("sample_mail%H%M%S@sample.com")
        user_password = datetime.now().strftime("password%H%M%S")
        login_page.register_new_user(user_email, user_password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link, timeout=5)
        page.open()
        page.verify_no_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link, timeout=5)
        page.open()
        page.click_add_to_basket_button()
        page.verify_product_name_added_to_basket()
        page.verify_product_price_added_to_basket()
