# -*- coding: utf-8 -*-
import logging
from tests_selenium_iFrame.pages.frame_page import FramePage
from tests_selenium_iFrame.utils.settings_parser import SettingsParser
from tests_selenium_iFrame.utils.get_random_text import get_random_text


class TestIframe:
    test_settings = SettingsParser().get_test_settings()
    logging.basicConfig(filename=test_settings['log_filename'], level=logging.INFO,
                        format=test_settings['log_format'])
    logger = logging.getLogger(__name__)

    def test_iframe(self):

        self.logger.info('Шаг 1. Открытие FramePage')

        frame_page = FramePage(self.test_settings)
        assert frame_page.is_opened(), self.logger.error("Frame page не открылась")

        self.logger.info('Шаг 2. Отправка рандомного текста и проверка его')

        text = get_random_text()
        frame_page.type_text(text)
        assert frame_page.get_text() == text

        self.logger.info('Шаг 3. Сделать текст жирным')

        frame_page.do_text_bold()
        assert frame_page.is_text_bold(), self.logger.error("Текст не жирный")
