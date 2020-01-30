import random
import string
from test_rest_api_get_post.models.post import Post
from test_rest_api_get_post.models.user import User


class TestHelper:

    @staticmethod
    def check_xml(content, key='sort'):
        if key == 'sort':
            keys = list(content.keys())
            return keys == sorted(keys)

    @staticmethod
    def get_books_with_certain_price(content, tag, key='max'):
        keys = list(content.keys())
        if key == 'max':
            return max([content[x][tag] for x in keys])
        if key == 'min':
            return min([content[x][tag] for x in keys])

    @staticmethod
    def add_post_instance(content):
        if type(content) == list:
            return [Post(data['userId'], data['id'], data['title'], data['body']) for data in content]
        else:
            return Post(content['userId'], content['id'], content['title'], content['body'])

    @staticmethod
    def check_posts(model, key='sort'):
        if key == 'sort':
            return [x.get_id() for x in model] == sorted([x.get_id() for x in model])

    @staticmethod
    def add_user_instance(content):
        if type(content) == list:
            return [User(data['id'],
                         data['name'],
                         data['username'],
                         data['email'],
                         data['address'],
                         data['phone'],
                         data['website'],
                         data['company'])
                    for data in content]
        else:
            return User(content['id'],
                        content['name'],
                        content['username'],
                        content['email'],
                        content['address'],
                        content['phone'],
                        content['website'],
                        content['company'])

    @staticmethod
    def get_string(size):
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))

    @staticmethod
    def check_json(file):
        marker = True
        for x in file:
            if type(x) is not dict:
                marker = False
        return marker
