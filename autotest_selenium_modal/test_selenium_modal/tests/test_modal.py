from test_selenium_modal.pages.main_page import MainPage
from test_selenium_modal.utils.settings_parser import SettingsParser
from test_selenium_modal.utils.string_utils import StringUtils
from framework.utils.alert import Alert
import allure
from hamcrest import assert_that
from hamcrest import equal_to, is_


class TestModal:
    settings = SettingsParser().get_test_settings()
    __LEN_STRING = 20

    @allure.feature("Тестирование страницы с модальными окнами")
    @allure.story("Тестирование взаимодействия с alert, confirm, prompt")
    def test_modal(self):
        with allure.step(f"Шаг 1. Проверка алерта на соответствие текста {self.settings['exp_alert_message']}"):
            main_page = MainPage()
            assert_that(main_page.is_opened(), is_(True), "MainPage не открылась")
            main_page.click_button_by_text(main_page.BTN_JS_ALERT)
            alert_text = Alert.get_alert_text()
            assert_that(alert_text, equal_to(self.settings['exp_alert_message']),
                        f"Текст не соответствует {self.settings['exp_alert_message']}")

        with allure.step("Шаг 2. Закрытие алерта"):
            Alert.close_alert()
            alert_result_text = main_page.get_result()
            assert_that(alert_result_text, equal_to(self.settings['alert_result']),
                        f"Текст не соответствует {self.settings['alert_result']}")

        with allure.step(f"Шаг 3. Проверка алерта на соответствие текста {self.settings['exp_confirm_message']}"):
            main_page.click_button_by_text(main_page.BTN_CONFIRM_ALERT)
            confirm_text = Alert.get_alert_text()
            assert_that(confirm_text, equal_to(self.settings['exp_confirm_message']),
                        f"Текст не соответствует {self.settings['exp_confirm_message']}")

        with allure.step("Шаг 4. Закрытие алерта"):
            Alert.close_alert()
            confirm_result_text = main_page.get_result()
            assert_that(confirm_result_text, equal_to(self.settings['confirm_result']),
                        f"Текст не соответствует {self.settings['confirm_result']}")

        with allure.step(f"Шаг 5. Проверка алерта на соответствие текста {self.settings['exp_prompt_message']}"):
            main_page.click_button_by_text(main_page.BTN_PROMPT_ALERT)
            prompt_text = Alert.get_alert_text()
            assert_that(prompt_text, equal_to(self.settings['exp_prompt_message']),
                        f"Текст не соответствует {self.settings['exp_prompt_message']}")

        with allure.step("Шаг 6. Проверка случайно введеного текста"):
            text = StringUtils().get_random_string(self.__LEN_STRING)
            Alert.send_text(text)
            Alert.close_alert()
            prompt_result_text = main_page.get_result()
            assert_that(prompt_result_text, equal_to(self.settings['prompt_result'] + text),
                        f"Текст не соответствует {self.settings['prompt_result'] + text}")
