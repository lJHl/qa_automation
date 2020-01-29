# -*- coding: utf-8 -*-
import json


class ConfigParser:
    """
    Class to parse configuration
    """
    def __init__(self):
        """
        Constructor to initialize settings
        """
        self.config_settings = self.config_reader("resourses/configuration.json")

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
