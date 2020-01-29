# -*- coding: utf-8 -*-
from web_framework.elements.base_element import BaseElement
from web_framework.waitings.custom_waitings import CustomWaitings
from selenium.webdriver.support import expected_conditions as EC


class Frame(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)

    def switch_to_frame(self):
        return CustomWaitings().fluent_wait().until(EC.frame_to_be_available_and_switch_to_it(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")
