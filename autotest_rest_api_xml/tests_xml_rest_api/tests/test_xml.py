from framework.utils.api_utils import APIUtils
from framework.utils.xml_parser import XmlParser
from framework.constants import status_code as SC
from framework.constants import extension as EX
from tests_xml_rest_api.utils.test_helper import TestHelper
from tests_xml_rest_api.utils.settings_parser import SettingsParser
import allure
from hamcrest import assert_that, equal_to, is_not


class TestXml:
    @allure.feature("Тестирование взаимодействия rest api с xml файлом")
    def test_xml_with_rest_api(self):

        with allure.step("Шаг 1. Проверить статус код"):
            settings = SettingsParser().get_test_settings()
            api = APIUtils(settings['request'])
            response = api.get()
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_OK),
                        f"Статус код отличается от {SC.STATUS_CODE_OK}")

        with allure.step("Шаг 2. Проверить расширение файла"):
            TestHelper().download_xml(response)
            assert_that(TestHelper.is_xml_extension(settings['xml']), equal_to(True),
                        f"Расширение файла не {EX.XML_EXTENSION}")
            xml = XmlParser.convert_xml_to_dict(settings['xml'])

        with allure.step("Шаг 3. Проверить что xml отсортирован"):
            books = TestHelper.add_book_instance(xml)
            assert_that(TestHelper.check_books_id(books), equal_to(True), "Список не отсортирован")

        with allure.step("Шаг 4. Проверить книги с высокой и низкой ценой"):
            max_price = max([x.get_price() for x in books])
            min_price = min([x.get_price() for x in books])
            assert_that(max_price, is_not(equal_to(min_price)), "Цены совпадают")
