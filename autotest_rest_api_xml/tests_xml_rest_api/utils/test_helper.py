from tests_xml_rest_api.models.book import Book
from tests_xml_rest_api.utils.settings_parser import SettingsParser
from framework.utils.xml_parser import XmlParser


class TestHelper:
    settings = SettingsParser().get_test_settings()

    @staticmethod
    def check_books_id(model, key='sort'):
        if key == 'sort':
            return [x.get_id() for x in model] == sorted([x.get_id() for x in model])

    @staticmethod
    def add_book_instance(content):
        return [Book(x['@id'], x['price']) for x in content['catalog']['book']]

    def download_xml(self, response):
        with open(self.settings['xml'], 'wb') as file:
            file.write(response.content)

    @staticmethod
    def is_xml_extension(path):
        try:
            XmlParser.convert_xml_to_dict(path)
        except Exception:
            return False
        return True
