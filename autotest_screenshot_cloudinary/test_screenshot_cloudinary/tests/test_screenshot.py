from framework.utils.api_utils import APIUtils
from framework.config.urls import Urls
from framework.utils.screenshooter import Screenshooter
from test_screenshot_cloudinary.pages.main_page import MainPage
from test_screenshot_cloudinary.utils.test_helper import TestHelper
from framework.config.cloudinary import CloudinaryConfig
from test_screenshot_cloudinary.utils.settings_parser import SettingsParser
import cloudinary.uploader
import allure
from hamcrest import assert_that, equal_to
import os


class TestScreenshot:

    __LEN_STRING = 20

    def test_screenshot(self):
        with allure.step(f"Шаг 1. Проверка открытия страницы {Urls.TEST_STAND_URL}"):
            settings = SettingsParser().get_test_settings()
            main_page = MainPage(settings)
            assert_that(main_page.is_opened(), equal_to(True), "Страница не открылась")

        with allure.step("Шаг 2. Ввод случайно сгенерированног текста"):
            text = TestHelper.get_random_string(self.__LEN_STRING)
            main_page.frame.send_text(text)
            assert_that(main_page.frame.get_text(), equal_to(text), "Текст не совпадает")

        with allure.step("Шаг 3. Проверка, что введенный текст жирный"):
            main_page.frame.do_text_bold()
            assert_that(main_page.frame.is_text_bold(), equal_to(True), "Введенный текст не жирный")

        with allure.step("Шаг 4. Создание скриншота"):
            Screenshooter.set_session_screen_dir()
            Screenshooter.take_screenshot()

            result = cloudinary.uploader.upload(os.path.join(Screenshooter.get_screen_session_dir(),
                                                             Screenshooter.get_screen_file_name()),
                                                public_id=CloudinaryConfig.PUBLIC_ID)

            api = APIUtils(result['url'])
            api.get_image()
            path_orig_img = os.path.join(Screenshooter.get_screen_session_dir(), Screenshooter.get_screen_file_name())
            path_download_img = os.path.join(Screenshooter.get_screen_session_dir(), settings['screen_file_name'])
            assert_that(TestHelper.check_image(path_orig_img, path_download_img), equal_to(True),
                        "Скриншоты неидентичны")
