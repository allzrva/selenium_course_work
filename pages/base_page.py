import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage(object):
    """
    Page Object for the base page of the web site
    """
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Opens the provided URL
        """
        self.browser.get(self.url)

    def go_to_basket_page(self):
        """
        Clicks on the basket button. Accessible from each page.
        :return: None
        """
        go_to_basket_btn = self.browser.find_element(*BasePageLocators.GO_TO_BASKET_BTN)
        go_to_basket_btn.click()

    def go_to_login_page(self):
        """
        Clicks on the Login option button. Accessible from each page.
        :return: None
        """
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_element_present(self, by_x, selector_str):
        """
        Verifies presence of the element on the web page

        :param by_x: strategy for elements location, e.g. By.CSS, By.ID
        :param selector_str: selector in form of a string
        :return: True if the element is found, False if not found
        """
        try:
            self.browser.find_element(by_x, selector_str)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, by_x, selector_str, timeout=4):
        """
        Verifies absence of the element on the web page

        :param by_x: strategy for elements location, e.g. By.CSS, By.ID
        :param selector_str: selector in form of a string
        :param timeout: element presence waiting time in seconds, 4 seconds by default
        :return: True if the element is NOT found during timeout wait time,
                False if the element is found during timeout wait time
        """
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((by_x, selector_str)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by_x, selector_str, timeout=4):
        """
        Verifies disappearance of the element on the web page

        :param by_x: strategy for elements location, e.g. By.CSS, By.ID
        :param selector_str: selector in form of a string
        :param timeout: element disappearance waiting time in seconds, 4 seconds by default
        :return: True if the element has disappeared during timeout wait time, False if it has not disappeared
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((by_x, selector_str)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        """
        Verifies that there is a login option button on the top right of the screen of each page.
        :return: True if the Login element has been found on the page
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link element is absent"

    def should_be_authorized_user(self):
        """
        Verifies presence of the user icon element.
        :return: True if the user icon element is found
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented probably unauthorised user"

    def solve_quiz_and_get_code(self):
        """
        Method for tasks 4_3_2, 4_3_3. Parses text from alert pop up window, calculates math equation and inserts the result.
        To see printed lines, use -s option in the pytest command.
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(int(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
