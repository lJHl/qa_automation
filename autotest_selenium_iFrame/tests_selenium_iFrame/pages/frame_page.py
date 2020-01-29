# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from web_framework.pages.base_page import BasePage
from web_framework.elements.block_element import BlockElement
from web_framework.elements.clickable_element import ClickableElement
from web_framework.elements.frame import Frame
from web_framework.browser.browser import Browser


class FramePageLocators:

    LOCATOR_FRAME_PAGE = (By.ID, "mceu_13")
    LOCATOR_FRAME_PAGE_IFRAME = (By.ID, "mce_0_ifr")
    LOCATOR_FRAME_PAGE_TEXT = (By.ID, "tinymce")
    LOCATOR_FRAME_PAGE_BOLD_TEXT = (By.XPATH, "//body[contains(@id, 'tinymce')]/p/strong")
    LOCATOR_FRAME_PAGE_BOLD_BUTTON = (By.XPATH, "//i[contains(@class, 'mce-i-bold')]")


class FramePage(BasePage):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings

    def is_opened(self):
        """
        method to check the page is opened

        :return: if the page is opened then return true or not return false
        """
        return BlockElement(FramePageLocators.LOCATOR_FRAME_PAGE).find_element_visibility()

    def type_text(self, text):
        """
        method to send random text

        :return: text
        """
        Frame(FramePageLocators.LOCATOR_FRAME_PAGE_IFRAME).switch_to_frame()
        element = BlockElement(FramePageLocators.LOCATOR_FRAME_PAGE_TEXT).find_element_visibility()
        element.clear()
        element.send_keys(text)
        Browser().switch_to_default_frame()
        return text

    def get_text(self):
        """
        method to check text

        :return: text
        """
        Frame(FramePageLocators.LOCATOR_FRAME_PAGE_IFRAME).switch_to_frame()
        text = BlockElement(FramePageLocators.LOCATOR_FRAME_PAGE_TEXT).find_element_visibility().text
        Browser().switch_to_default_frame()
        return text

    def do_text_bold(self):
        """
        method to do text bold
        """
        Frame(FramePageLocators.LOCATOR_FRAME_PAGE_IFRAME).switch_to_frame()
        element = BlockElement(FramePageLocators.LOCATOR_FRAME_PAGE_TEXT).find_element_visibility()
        element.click()
        element.send_keys(Keys.CONTROL + self.settings['KEY_a'])
        Browser().switch_to_default_frame()
        ClickableElement(FramePageLocators.LOCATOR_FRAME_PAGE_BOLD_BUTTON).find_element_clickable().click()

    def is_text_bold(self):
        """
        method to check text is bold

        :return: if the text is bold then return true or not return false
        """
        Frame(FramePageLocators.LOCATOR_FRAME_PAGE_IFRAME).switch_to_frame()
        return BlockElement(FramePageLocators.LOCATOR_FRAME_PAGE_BOLD_TEXT).find_element_visibility()
