# -*- coding: utf-8 -*-
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from web_framework.browser.browser import Browser
from web_framework.waitings.custom_waitings import CustomWaitings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BaseElement:
    """
    Class for base element
    """
    def __init__(self, locator):
        """
        Constructor to initialize web driver, locator and waiting

        :param locator: locator for element
        """
        self.driver = Browser().get_driver()
        self.locator = locator
        self.wait = CustomWaitings()

    def find_element_located(self):
        """
        method to look for element by locator
        """
        return self.wait.fluent_wait().until(EC.presence_of_element_located(self.locator),
                                        message=f"Can't find element by locator {self.locator}")

    def find_elements_located(self):
        """
        method to look for elements by locator
        """
        return self.wait.fluent_wait().until(EC.presence_of_all_elements_located(self.locator),
                                        message=f"Can't find elements by locator {self.locator}")

    def hover(self):
        """
        method to hover element by locator
        """
        target = self.find_element_located()
        y_position = 0
        searching = True
        while searching:
            try:
                ActionChains(self.driver).move_to_element(target).perform()
                searching = False
            except MoveTargetOutOfBoundsException:
                y_position += 500
                self.driver.execute_script('window.scrollTo(0, ' + str(y_position) + ');')
