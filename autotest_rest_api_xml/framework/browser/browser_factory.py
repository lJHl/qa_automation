# coding=utf-8
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.config.browser import BrowserConfig, Selenoid
from framework.constants import browsers
from os import environ


class BrowserFactory:

    @staticmethod
    def get_browser_driver(selenoid, browser_key, lang, capabilities, is_incognito, enable_performance_logging, test_name):
        if capabilities is None:
            capabilities = {}
        if browser_key == browsers.BROWSER_CHROME:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', False)
            options.add_argument(f"--lang={lang}")

            if is_incognito:
                options.add_argument("--incognito")
            if enable_performance_logging:
                capabilities['loggingPrefs'] = {'performance': 'ALL'}
            if selenoid:
                return BrowserFactory.get_remote_driver(browser_name=browser_key,
                                                        browser_version=BrowserConfig.CHROME_VERSION,
                                                        options=options, capabilities=capabilities,
                                                        test_name=test_name, url=Selenoid.SELENOID_URL)
            else:
                return webdriver.Chrome(ChromeDriverManager().install(), options=options,
                                        desired_capabilities=capabilities)

        elif browser_key == browsers.BROWSER_FIREFOX:
            options = webdriver.FirefoxOptions()
            if is_incognito:
                options.set_preference("browser.privatebrowsing.autostart", True)
                options.set_preference("intl.accept_languages", lang)
            if enable_performance_logging:
                open("perfLog.txt", "w").close()
                environ["MOZ_LOG"] = "timestamp,sync,nsHttp:3"
            if selenoid:
                return BrowserFactory.get_remote_driver(browser_name=browser_key,
                                                        browser_version=BrowserConfig.FIREFOX_VERSION,
                                                        options=options, capabilities=capabilities,
                                                        test_name=test_name, url=Selenoid.SELENOID_URL)
            else:
                return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                         options=options, desired_capabilities=capabilities)

    @staticmethod
    def get_remote_driver(browser_name, browser_version, url, options=None, capabilities=None,
                          test_name=None):
        if capabilities is None:
            capabilities = {}
        capabilities["browserName"] = browser_name
        capabilities["version"] = browser_version
        capabilities["name"] = test_name
        return webdriver.Remote(command_executor=url,
                                desired_capabilities=capabilities, options=options)
