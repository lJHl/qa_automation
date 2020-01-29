# -*- coding: utf-8 -*-
import allure
from framework.cookie_tool.cookie_tool import CookieTool
from tests_cookie.pages.example_page import ExamplePage
from tests_cookie.utilities.settings_parser import SettingsParser


class TestCookie:
    def test_selenium_cookie(self):

        with allure.step('Шаг 1. Открыть главную страницу'):
            example_page = ExamplePage()
            assert example_page.is_opened(), 'Страница не открылась'

        with allure.step('Шаг 2. Добавить cookie'):
            settings = SettingsParser().get_test_settings()
            cookies = settings['cookies']
            CookieTool().add_cookie(cookies)
            assert CookieTool().is_cookies_match(cookies), "Cookies не были добавлены"

        with allure.step('Шаг 3. Удалить cookie'):
            CookieTool().delete_cookie(settings['cookie_for_delete'])
            assert CookieTool().is_cookies_match(
                [x for x in cookies if x['name'] != settings['cookie_for_delete']]), \
                "Cookie не был удален"

        with allure.step('Шаг 4. Обновить cookie'):
            CookieTool().update_cookie(settings['cookie_for_update'])
            assert CookieTool().is_cookies_match([settings['cookie_for_update']]), \
                "Cookie не был изменен"

        with allure.step('Шаг 5. Удалить все cookies'):
            CookieTool().delete_all_cookies()
            assert not CookieTool().get_cookies(), "Cookie не были удалены"
