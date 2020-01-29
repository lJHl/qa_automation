# -*- coding: utf-8 -*-
from random import choice
from string import ascii_lowercase


def get_random_text():
    """
    Function to return random text

    :return: random text
    """
    return ''.join(choice(ascii_lowercase) for i in range(20))
