# -*- coding: utf-8 -*-
import json
import os
from web_framework.singleton import Singleton


class ConfigParser(metaclass=Singleton):
    """
    Class to parse configuration
    """
    def __init__(self):
        """
        Constructor to initialize settings
        """
        os.chdir("..")
        self.config_settings = self.config_reader("tests_selenium_iFrame/resources/configuration.json")

    @staticmethod
    def config_reader(path):
        """
        Function to read config from json file

        :path: path to file
        :return: dict of settings
        """
        try:
            with open(path, "r", encoding="UTF-8") as s:
                settings = json.load(s)
        except FileNotFoundError as e:
            print(e)
        else:
            return settings

    def get_config_settings(self):
        """
        method to return configuration settings

        :return: configuration settings
        """
        return self.config_settings
