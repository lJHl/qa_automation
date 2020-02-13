from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from framework.elements.link import Link
from framework.elements.button import Button
from framework.elements.block import Block
from framework.elements.text_box import TextBox
from framework.utils.rest_api import APIUtils


class MainPageLocators:
    MAIN_PAGE = "//div[@id='pageContent']"
    OBJECT_CODING_LABLE = "//div[contains(@class, 'formBody')]/div"
    OBJECT_CODING_LINK = "//a[text()='{text}']"
    INPUT = "//input[@name='l']"
    SUBMIT_BUTTON = "//input[@type='submit']"
    QR_CODE = "//div[contains(@class, 'image')]/img"


class MainPage(BasePage):
    __INPUT = TextBox(By.XPATH, MainPageLocators.INPUT, "Input field")
    __SUBMIT = Button(By.XPATH, MainPageLocators.SUBMIT_BUTTON, "Submit button")
    __QR_CODE = Link(By.XPATH, MainPageLocators.QR_CODE, "QR code")

    def __init__(self):
        super().__init__(By.XPATH, MainPageLocators.MAIN_PAGE, "Main page")

    def change_type_coding(self, text):
        Link(By.XPATH, MainPageLocators.OBJECT_CODING_LINK.format(text=text), "Type coding link").click()

    def is_type_change(self, text):
        if Block(By.XPATH, MainPageLocators.OBJECT_CODING_LABLE.format(text=text), "Type coding text").get_text() == text:
            return True
        else:
            return False

    def enter_link(self, text):
        self.__INPUT.clear_field()
        self.__INPUT.send_keys(text)
        self.__SUBMIT.click()

    def get_qr_code(self):
        url = self.__QR_CODE.get_attribute('src')
        return APIUtils.get_image(url)