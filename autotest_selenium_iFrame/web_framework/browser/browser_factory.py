# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from web_framework.utilities.config_parser import ConfigParser


class BrowserFactory:
    """
    Browser factory pattern
    """
    def __init__(self):
        """
        Constructor for pattern
        """
        self.config_settings = ConfigParser().get_config_settings()
        self.download_dir = self.__get_download_dir()

    def get_driver(self):
        """
        method to return driver

        :return: driver
        """
        if self.config_settings['browser'].lower() == "chrome":
            return self.__get_chrome_driver()
        elif self.config_settings['browser'].lower() == "firefox":
            return self.__get_firefox_driver()
        else:
            raise Exception("This browser doesn't exist")

    def __get_download_dir(self):
        download_dir = self.config_settings['download_dir']
        if download_dir == 'default':
            return os.getcwd()
        else:
            return download_dir

    def __get_chrome_driver(self):
        """
        method to return chrome driver
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs',
                                        {"download.default_directory": self.download_dir,
                                         "download.directory_upgrade": True,
                                         "safebrowsing.enabled": True
                                         })
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    def __get_firefox_driver(self):
        """
        method to return firefox driver
        """
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", os.getcwd())
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
