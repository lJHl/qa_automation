# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from test_screenshot_cloudinary.pages.frame import Frame


class MainPageLocators:

    LOCATOR_MAIN_PAGE = "//div[contains(@class, 'example')]"


class MainPage(BasePage):
    def __init__(self, settings):
        super().__init__(By.XPATH, MainPageLocators.LOCATOR_MAIN_PAGE, "MainPage")
        self.settings = settings
        self.frame = Frame(settings)
