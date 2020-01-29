from framework.utils.api_utils import APIUtils
from framework.config.urls import Urls
from test_basic_authorization.utils.settings_parser import SettingsParser
import allure
from hamcrest import *


class TestXml:
    @allure.feature("Тестирование базовой авторизации")
    def test_basic_authorization(self):
        with allure.step(f"Прохождение авторизации на ресурсе {Urls.TEST_STAND_URL}"):
            settings = SettingsParser().get_test_settings()
            api = APIUtils(Urls.TEST_STAND_URL)
            api.get(auth=(settings['login'], settings['password']))
            assert_that(settings['template'], equal_to(api.get_content_json()), "Данные не совпадают")
