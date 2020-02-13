import allure
from hamcrest import assert_that, equal_to
from test_qr_code.pages.main_page import MainPage
from test_qr_code.resources.test_settings import Test_settings
from framework.utils.qr_reader import QRReader


class TestQRCode:
    @allure.feature("Тестирование кодирования qr кода на сайте http://qrcoder.ru/")
    def test_creation_qr_code(self):
        with allure.step("Шаг 1. Открытие главной страницы"):
            main_page = MainPage()
            assert_that(main_page.is_opened(), equal_to(True), "Главная страница не открылась")

        with allure.step(f"Шаг 2. Изменение объекта кодирования на {Test_settings.OBJECT_CODING}"):
            main_page.change_type_coding(Test_settings.OBJECT_CODING)
            assert_that(main_page.is_type_change(Test_settings.OBJECT_VALIDATION), equal_to(True), "Объект кодирования не изменился")

        with allure.step("Шаг 3. Создание qr кода"):
            main_page.enter_link(Test_settings.TEXT_FOR_CODING)
            path_to_qr = main_page.get_qr_code()
            r = QRReader.read_qr(path_to_qr)
            assert_that(r['type'], equal_to(Test_settings.TYPE), "Код не создан")

        with allure.step("Шаг 4. Проверка url из qr кода"):
            assert_that(r['data'], equal_to(Test_settings.TEXT_FOR_CODING), "Url отличается")