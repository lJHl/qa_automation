# -*- coding: utf-8 -*-
from web_framework.elements.base_element import BaseElement
from web_framework.waitings.custom_waitings import CustomWaitings
from selenium.webdriver.support import expected_conditions as EC


class BlockElement(BaseElement):
    """
    Class for Block element
    """
    def __init__(self, locator):
        """
        Constructor for class

        :param locator: element locator
        """
        super().__init__(locator)

    def find_element_visibility(self):
        """
        method to look for element
        """
        return CustomWaitings().fluent_wait().until(EC.visibility_of_element_located(self.locator),
                                               message=f"Can't find element by locator {self.locator}")

    def find_element_not_visibility(self):
        """
        method to look for element
        """
        return CustomWaitings().error_wait().until_not(EC.visibility_of_element_located(self.locator),
                                                     message=f"Can't find element by locator {self.locator}")
