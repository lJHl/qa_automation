import pytest
import allure
from framework.browser.browser import Browser
from framework.config.browser import BrowserConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BrowserConfig.BROWSER,
                     help="Name of browser")
    parser.addoption("--selenoid", action="store", default=False,
                     help="Use selenoid connection")
    parser.addoption("--lang", action="store", default=BrowserConfig.LANG,
                     help="Browser language")


@pytest.fixture(scope="function", autouse=False)
def create_browser(request):
    with allure.step("Creating a browser session"):
        browser = request.config.getoption('--browser')
        selenoid = request.config.getoption('--selenoid')
        lang = request.config.getoption('--lang')
        Browser.get_browser().set_up_driver(browser_key=browser, selenoid=selenoid, lang=lang)

    yield

    with allure.step("Close sessions of all browsers"):
        for browser_key in list(Browser.get_browser().get_driver_names()):
            Browser.get_browser().quit(browser_key=browser_key)
