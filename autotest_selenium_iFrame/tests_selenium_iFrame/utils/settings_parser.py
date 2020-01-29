# -*- coding: utf-8 -*-
from web_framework.singleton import Singleton
import json


class SettingsParser(metaclass=Singleton):
    """
    Class to parse test setting
    """
    def __init__(self):
        """
        Constructor to initialize settings
        """
        self.test_settings = self.settings_reader("resources/test_settings.json")

    @staticmethod
    def settings_reader(path):
        """
        Function to read test settings from json file

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

    def get_test_settings(self):
        """
        method to return test settings

        :return: test settings
        """
        return self.test_settings
