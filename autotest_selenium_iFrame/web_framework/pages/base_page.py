# -*- coding: utf-8 -*-
from web_framework.browser.browser import Browser


class BasePage:
    """
    Base class for pages
    """
    def __init__(self):
        """
        Constructor for class
        """
        self.driver = Browser().get_driver()

    def is_opened(self):
        """
        method to check the page is opened

        :return: page title
        """
        return self.driver.title
