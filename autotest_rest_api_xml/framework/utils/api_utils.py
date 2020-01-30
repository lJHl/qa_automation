import requests


class APIUtils:
    def __init__(self, req):
        self.req = req
        self.status_code = ''
        self.content_string = ''

    def get(self):
        r = requests.get(self.req)
        self.status_code = r.status_code
        self.content_string = r.text
        return r

    def get_status_code(self):
        return self.status_code

    def get_content_string(self):
        return self.content_string
