import os
import pytest
import allure
from test_test_rail.resources.results import Results
from framework.browser.browser import Browser
from framework.config.browser import BrowserConfig
from framework.utils.screenshooter import Screenshooter
from framework.config.testrail import TestRailConfig
from framework.testrail.api.testrail_api import TestRailApi
from framework.constants import testrail as TR


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BrowserConfig.BROWSER,
                     help="Name of browser")
    parser.addoption("--selenoid", action="store", default=False,
                     help="Use selenoid connection")
    parser.addoption("--lang", action="store", default=BrowserConfig.LANG,
                     help="Browser language")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
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


@pytest.fixture(scope="function", autouse=True)
def send_result_to_testrail(request):
    yield
    with allure.step("Sending results to testrail"):
        Screenshooter.set_session_screen_dir()
        Screenshooter.take_screenshot()
        path = os.path.join(Screenshooter.get_screen_session_dir(),
                            Screenshooter.get_screen_file_name())

        if request.node.rep_call.failed:
            status = TR.STATUS_FAILED
            comment = TR.COMMENT_FAILED
        elif request.node.rep_call.passed:
            status = TR.STATUS_PASSED
            comment = TR.COMMENT_PASSED

        api = TestRailApi(TestRailConfig.TESTRAIL_URL, TestRailConfig.USER, TestRailConfig.PASSWORD)
        result = api.add_result(TestRailConfig.TEST_ID, status_id=status, comment=comment, custom_step_results=Results.test_modal_result)
        api.add_attachment_to_result(result['id'], path)
