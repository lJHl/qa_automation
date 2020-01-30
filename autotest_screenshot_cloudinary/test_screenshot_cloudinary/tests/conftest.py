import pytest
import allure
import cloudinary
from framework.browser.browser import Browser
from framework.config.browser import BrowserConfig
from framework.config.cloudinary import CloudinaryConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BrowserConfig.BROWSER,
                     help="Name of browser")
    parser.addoption("--selenoid", action="store", default=False,
                     help="Use selenoid connection")
    parser.addoption("--lang", action="store", default=BrowserConfig.LANG,
                     help="Browser language")


@pytest.fixture(scope="function", autouse=True)
def create_browser(request):
    with allure.step("Creating a browser session"):
        browser = request.config.getoption('--browser')
        selenoid = request.config.getoption('--selenoid')
        lang = request.config.getoption('--lang')
        Browser.get_browser().set_up_driver(browser_key=browser, selenoid=selenoid, lang=lang)
        cloudinary.config(
            cloud_name=CloudinaryConfig.CLOUD_NAME,
            api_key=CloudinaryConfig.API_KEY,
            api_secret=CloudinaryConfig.API_SECRET
        )
    yield

    with allure.step("Close sessions of all browsers"):
        for browser_key in list(Browser.get_browser().get_driver_names()):
            Browser.get_browser().quit(browser_key=browser_key)
