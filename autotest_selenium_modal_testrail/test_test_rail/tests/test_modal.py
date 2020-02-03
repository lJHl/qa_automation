from test_test_rail.pages.main_page import MainPage
from test_test_rail.utils.string_utils import StringUtils
from test_test_rail.resources.test_settings import TestSettings
from test_test_rail.resources.results import Results
from framework.utils.alert import Alert
import allure
from hamcrest import assert_that, equal_to


class TestModal:
    __LEN_STRING = 20
    __STEP_ONE = f"Шаг 1. Проверка алерта на соответствие текста {TestSettings.exp_alert_message}"
    __STEP_TWO = "Шаг 2. Закрытие алерта"
    __STEP_THREE = f"Шаг 3. Проверка алерта на соответствие текста {TestSettings.exp_confirm_message}"
    __STEP_FOUR = "Шаг 4. Закрытие алерта"
    __STEP_FIVE = f"Шаг 5. Проверка алерта на соответствие текста {TestSettings.exp_prompt_message}"
    __STEP_SIX = "Шаг 6. Проверка случайно введеного текста"

    @allure.story("Тестирование страницы с модальными окнами")
    @allure.feature("Тестирование взаимодействия с alert, confirm, prompt")
    def test_modal(self, tmpdir):
        with allure.step(self.__STEP_ONE):
            main_page = MainPage()
            assert_that(main_page.is_opened(), equal_to(True), "MainPage не открылась")
            main_page.click_button_by_text(main_page.BTN_JS_ALERT)
            alert_text = Alert.get_alert_text()
            Results.test_modal_result.append({"content": self.__STEP_ONE, "expected": TestSettings.exp_alert_message, "actual": alert_text})
            assert_that(alert_text, equal_to(TestSettings.exp_alert_message),
                        f"Текст не соответствует {TestSettings.exp_alert_message}")

        with allure.step(self.__STEP_TWO):
            Alert.close_alert()
            alert_result_text = main_page.get_result()
            Results.test_modal_result.append({"content": self.__STEP_TWO, "expected": TestSettings.alert_result, "actual": alert_result_text})
            assert_that(alert_result_text, equal_to(TestSettings.alert_result),
                        f"Текст не соответствует {TestSettings.alert_result}")

        with allure.step(self.__STEP_THREE):
            main_page.click_button_by_text(main_page.BTN_CONFIRM_ALERT)
            confirm_text = Alert.get_alert_text()
            Results.test_modal_result.append({"content": self.__STEP_THREE, "expected": TestSettings.exp_confirm_message, "actual": confirm_text})
            assert_that(confirm_text, equal_to(TestSettings.exp_confirm_message),
                        f"Текст не соответствует {TestSettings.exp_confirm_message}")

        with allure.step(self.__STEP_FOUR):
            Alert.close_alert()
            confirm_result_text = main_page.get_result()
            Results.test_modal_result.append({"content": self.__STEP_FOUR, "expected": TestSettings.confirm_result, "actual": confirm_result_text})
            assert_that(confirm_result_text, equal_to(TestSettings.confirm_result),
                        f"Текст не соответствует {TestSettings.confirm_result}")

        with allure.step(self.__STEP_FIVE):
            main_page.click_button_by_text(main_page.BTN_PROMPT_ALERT)
            prompt_text = Alert.get_alert_text()
            Results.test_modal_result.append({"content": self.__STEP_FIVE, "expected": TestSettings.exp_prompt_message, "actual": prompt_text})
            assert_that(prompt_text, equal_to(TestSettings.exp_prompt_message),
                        f"Текст не соответствует {TestSettings.exp_prompt_message}")

        with allure.step(self.__STEP_SIX):
            text = StringUtils().get_random_string(self.__LEN_STRING)
            Alert.send_text(text)
            Alert.close_alert()
            prompt_result_text = main_page.get_result()
            Results.test_modal_result.append({"content": self.__STEP_SIX, "expected": TestSettings.prompt_result + text, "actual": prompt_result_text})
            assert_that(prompt_result_text, equal_to(TestSettings.prompt_result + text),
                        f"Текст не соответствует {TestSettings.prompt_result + text}")
