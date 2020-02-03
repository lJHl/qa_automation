from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.button import Button
from framework.elements.block import Block


class MainPageLocators:
    LOCATOR_MAIN_PAGE = "//div[contains(@id, 'content')]"
    LOCATOR_MAIN_PAGE_BUTTON = "//button[contains(text(), '{text}')]"
    LOCATOR_MAIN_PAGE_RESULT = "//p[contains(@id, 'result')]"


class MainPage(BasePage):
    BTN_JS_ALERT = "Click for JS Alert"
    BTN_CONFIRM_ALERT = "Click for JS Confirm"
    BTN_PROMPT_ALERT = "Click for JS Prompt"
    __RESULT = Block(By.XPATH, MainPageLocators.LOCATOR_MAIN_PAGE_RESULT, "Result text")

    def __init__(self):
        super().__init__(By.XPATH, MainPageLocators.LOCATOR_MAIN_PAGE, "MainPage")

    def click_button_by_text(self, text):
        button = Button(By.XPATH, MainPageLocators.LOCATOR_MAIN_PAGE_BUTTON.
                        format(text=text), f"{text} button")
        button.click()

    def get_result(self):
        return self.__RESULT.get_text()
