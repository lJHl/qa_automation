# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser
from framework.elements.button import Button
from framework.elements.text_box import TextBox


class FrameLocators:
    LOCATOR_FRAME_IFRAME = "//iframe[contains(@id, 'mce_0_ifr')]"
    LOCATOR_FRAME_TEXT = "//body[contains(@id, 'tinymce')]"
    LOCATOR_FRANE_BOLD_TEXT = "//body[contains(@id, 'tinymce')]/p/strong"
    LOCATOR_FRAME_BOLD_BUTTON = "//i[contains(@class, 'mce-i-bold')]"


class Frame:
    __TEXT_FIELD = TextBox(By.XPATH, FrameLocators.LOCATOR_FRAME_TEXT, "Text field")
    __IFRAME = By.XPATH, FrameLocators.LOCATOR_FRAME_IFRAME
    __BOLD_BUTTON = Button(By.XPATH, FrameLocators.LOCATOR_FRAME_BOLD_BUTTON, "Bold button")
    __BOLD_TEXT = TextBox(By.XPATH, FrameLocators.LOCATOR_FRANE_BOLD_TEXT, "Bold text")

    def __init__(self, settings):
        self.settings = settings

    def send_text(self, text):
        """
        method to send random text
        """
        Browser().switch_to_frame_by_locator(*self.__IFRAME)
        element = self.__TEXT_FIELD
        element.selenium_clear()
        element.send_keys(text)
        Browser().switch_to_default_content()

    def get_text(self):
        """
        method to get text

        :return: text
        """
        Browser().switch_to_frame_by_locator(*self.__IFRAME)
        text = self.__TEXT_FIELD.find_element().text
        Browser().switch_to_default_content()
        return text

    def do_text_bold(self):
        """
        method to do text bold
        """
        Browser().switch_to_frame_by_locator(*self.__IFRAME)
        element = self.__TEXT_FIELD.find_element()
        element.send_keys(Keys.CONTROL + self.settings['KEY_a'])
        Browser().switch_to_default_content()
        self.__BOLD_BUTTON.click()

    def is_text_bold(self):
        """
        method to check text is bold

        :return: if the text is bold then return true or not return false
        """
        Browser().switch_to_frame_by_locator(*self.__IFRAME)
        if self.__BOLD_TEXT.find_element():
            return True
        else:
            return False
