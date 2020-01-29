# -*- coding: utf-8 -*-
from framework.browser.browser import Browser


class CookieTool:
    def __init__(self):
        self.driver = Browser().get_driver()

    def add_cookie(self, cookie):
        for c in cookie:
            self.driver.add_cookie(c)

    def get_cookies(self):
        return self.driver.get_cookies()

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def update_cookie(self, cookie):
        cookie_for_update = self.driver.get_cookie(cookie['name'])
        self.delete_cookie(cookie_for_update['name'])
        cookie_for_update['value'] = cookie['value']
        self.add_cookie([cookie_for_update])

    def is_cookies_match(self, cookies):
        get_cookies = CookieTool().get_cookies()
        get_cookies_keys = get_cookies.keys()

        for key in cookies.keys():
            if key in get_cookies_keys:
                if cookies.get(key) != get_cookies.get(key):
                    return False
            return False
        return True
