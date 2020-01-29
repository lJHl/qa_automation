import random
import string


class StringUtils:

    @staticmethod
    def get_random_string(size):
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))

