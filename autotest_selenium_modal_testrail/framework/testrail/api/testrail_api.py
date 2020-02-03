from framework.utils.testrail import APIClient
from framework.testrail.api.urls.urls import Urls


class TestRailApi:
    def __init__(self, url, user, password):
        self.client = APIClient(url)
        self.client.user = user
        self.client.password = password

    def add_result(self, test_id, **kwargs):
        return self.client.send_post(Urls.ADD_RESULT.format(test_id=test_id), kwargs)

    def add_attachment_to_result(self, id, path):
        return self.client.send_post(Urls.ADD_ATTACHMENT.format(id=id), path)
