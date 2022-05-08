from .base_page import BasePage


class MainPage(BasePage):
    """
    Page Object for the main page of the web site
    """
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
