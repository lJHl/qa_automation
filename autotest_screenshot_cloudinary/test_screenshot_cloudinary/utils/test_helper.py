import random
import string
from PIL import Image, ImageChops


class TestHelper:

    @staticmethod
    def get_random_string(size):
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))

    @staticmethod
    def check_image(img_1, img_2):
        im_1 = Image.open(img_1)
        im_2 = Image.open(img_2)
        return ImageChops.difference(im_1, im_2).getbbox() is None
