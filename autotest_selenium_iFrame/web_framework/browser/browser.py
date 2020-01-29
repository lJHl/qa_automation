# -*- coding: utf-8 -*-
from web_framework.singleton import Singleton
from web_framework.browser.browser_factory import BrowserFactory
from web_framework.utilities.config_parser import ConfigParser


class Browser(metaclass=Singleton):
    """
    Class to create browser instance
    """
    def __init__(self):
        """
        Constructor to initialize web driver
        """
        config_settings = ConfigParser().get_config_settings()
        self.base_url = config_settings['base_url']
        self.driver = BrowserFactory().get_driver()

    def get_driver(self):
        """
        method to return web driver

        :return: web driver
        """
        return self.driver

    def get_base_url(self):
        """
        method to get base url

        :return: base url
        """
        return self.driver.get(self.base_url)

    def switch_to_default_frame(self):
        """
        method to return base frame

        :return: base url
        """
        self.driver.switch_to_default_content()

    def quit(self):
        """
        method to quit driver
        """
        self.driver.quit()
