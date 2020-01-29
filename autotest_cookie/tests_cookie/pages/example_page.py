# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage


class ExamplePageLocators:

    LOCATOR_EXAMPLE_PAGE = '//div'


class ExamplePage(BasePage):
    def __init__(self):
        super().__init__(By.XPATH, ExamplePageLocators.LOCATOR_EXAMPLE_PAGE, 'ExamplePage')

    def is_opened(self):
        return super().is_opened()
