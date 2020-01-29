# -*- coding: utf-8 -*-
from web_framework.elements.base_element import BaseElement
from web_framework.waitings.custom_waitings import CustomWaitings
from selenium.webdriver.support import expected_conditions as EC


class ClickableElement(BaseElement):
    """
    Class for Clickable element
    """
    def __init__(self, locator):
        """
        Constructor for class

        :param locator: element locator
        """
        super().__init__(locator)

    def click(self):
        """
        method to click element
        """
        self.hover()
        self.find_element_clickable().click()

    def find_element_clickable(self):
        """
        method to look for element
        """
        return CustomWaitings().fluent_wait().until(EC.element_to_be_clickable(self.locator),
                                               message=f"Can't find element by locator {self.locator}")

    def find_element_not_clickable(self):
        """
        method to look for element
        """
        return CustomWaitings().error_wait().until_not(EC.element_to_be_clickable(self.locator),
                                                     message=f"Can't find element by locator {self.locator}")
