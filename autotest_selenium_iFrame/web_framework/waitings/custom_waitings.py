# -*- coding: utf-8 -*-
import os
from selenium.webdriver.support.wait import WebDriverWait
from web_framework.browser.browser import Browser
from web_framework.utilities.config_parser import ConfigParser
import time


class CustomWaitings:
    """
    Class for custom waitings
    """
    def __init__(self):
        """
        Constructor for class
        """
        self.config_settings = ConfigParser().get_config_settings()
        self.f_wait = self.config_settings['fluent_wait_time']
        self.err_wait = self.config_settings['error_wait_time']
        self.poll_frequency = self.config_settings['poll_frequency']
        self.driver = Browser().get_driver()

    def fluent_wait(self):
        """
        method to create fluent wait

        :return: fluent wait
        """
        return WebDriverWait(self.driver, self.f_wait, self.poll_frequency)

    def error_wait(self):
        """
        method to create error wait

        :return: error wait
        """
        return WebDriverWait(self.driver, self.err_wait)

    def download_wait(self, max_time=100):
        """
        method to create waiting for download
        """
        while True:
            if os.path.isfile(self.config_settings['steam_client_name']):
                break
            else:
                if max_time == 0:
                    break
                time.sleep(1)
                max_time -= 1
