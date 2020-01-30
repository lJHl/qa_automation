import requests
from framework.utils.screenshooter import Screenshooter
import os
from test_screenshot_cloudinary.utils.settings_parser import SettingsParser


class APIUtils:
    settings = SettingsParser().get_test_settings()

    def __init__(self, req):
        self.req = req
        self.status_code = ''
        self.content_string = ''
        self.content_json = ''

    def get(self, url):
        r = requests.get(self.req + url)
        self.status_code = r.status_code
        self.content_string = r.text
        self.content_json = r.json()
        return r

    def get_headers(self, req, header):
        return req.headers.get(header)

    def get_status_code(self):
        return self.status_code

    def get_content_string(self):
        return self.content_string

    def get_content_json(self):
        return self.content_json

    def post(self, url, data):
        r = requests.post(self.req + url, json=data)
        self.status_code = r.status_code
        self.content_string = r.text
        self.content_json = r.json()
        return r

    def post_headers(self, post, header):
        return post.headers.get(header)

    def get_image(self):
        r = requests.get(self.req)
        with open(os.path.join(Screenshooter.get_screen_session_dir(), self.settings['screen_file_name']), "wb") as out:
            out.write(r.content)
