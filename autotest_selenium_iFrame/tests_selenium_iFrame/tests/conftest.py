# -*- coding: utf-8 -*-
import pytest
from web_framework.browser.browser import Browser


@pytest.fixture(scope='function', autouse=True)
def setup():
    """
    Fixture for implementing setup and teardown
    """
    driver = Browser()
    driver.get_driver()
    driver.get_base_url()
    yield
    driver.quit()
