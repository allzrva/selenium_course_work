# Page Object for the base page of the web site
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_x, selector_str):
        try:
            self.browser.find_element(by_x, selector_str)
        except NoSuchElementException:
            return False
        return True

