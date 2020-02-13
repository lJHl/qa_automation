import requests
import os
from framework.config.rest_api import RestApiConfig


class APIUtils:

    @staticmethod
    def get(url, params=None, **kwargs):
        r = requests.get(url, params=params, **kwargs)
        return r

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        r = requests.post(url, data=data, json=json, **kwargs)
        return r

    @staticmethod
    def get_image(url):
        r = APIUtils.get(url)
        path = os.path.join(RestApiConfig.DOWNLOAD_DIR, RestApiConfig.FILENAME_PNG)
        with open(path, "wb") as out:
            out.write(r.content)
        return path
