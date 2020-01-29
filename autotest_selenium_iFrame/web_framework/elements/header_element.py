# -*- coding: utf-8 -*-
from web_framework.elements.base_element import BaseElement
from web_framework.waitings.custom_waitings import CustomWaitings
from selenium.webdriver.support import expected_conditions as EC
import logging


class HeaderElement(BaseElement):
    """
    Class for Header element
    """
    def __init__(self, locator):
        """
        Constructor for class

        :param locator: element locator
        """
        super().__init__(locator)

    def find_element_present_text(self, text):
        logger = logging.getLogger(__name__)
        logger.info(f'Looking for element with locator {self.locator}')
        return CustomWaitings().fluent_wait().until(EC.text_to_be_present_in_element(self.locator, text),
                                               message=f"Can't find element by locator {self.locator}")
