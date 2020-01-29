# -*- coding: utf-8 -*-
import random
import logging
from web_framework.elements.base_element import BaseElement
from web_framework.elements.clickable_element import ClickableElement
from selenium.webdriver.support.ui import Select


class SelectElement(BaseElement):
    """
    Class for select element
    """
    def __init__(self, locator):
        """
        Constructor for class

        :param locator: element locator
        """
        super().__init__(locator)

    def select_by_value(self, value):
        """
        method to select element by value

        :param value: value
        """
        logger = logging.getLogger(__name__)
        logger.info('Element selection')
        select = Select(self.find_element_located())
        select.select_by_value(value)

    def select_by_text(self, text):
        """
        method to select element by value

        :param text: text
        """
        logger = logging.getLogger(__name__)
        logger.info('Element selection')
        select = Select(self.find_element_located())
        logger.info(f'click() method for element with locator {self.locator}')
        ClickableElement(self.locator).click()
        select.select_by_visible_text(text)

    def get_random_category(self):
        """
        method to get random category

        :return: random category
        """
        logger = logging.getLogger(__name__)
        logger.info('Element selection')
        select = Select(self.find_element_located())
        return random.choice([elem.get_attribute('value') for elem in select.options
                              if elem.get_attribute('value') != '0'])

    def get_selected_option(self):
        """
        method to get selected option

        :return: selected option text
        """
        logger = logging.getLogger(__name__)
        logger.info('Element selection')
        select = Select(self.find_element_located())
        return select.first_selected_option.text
