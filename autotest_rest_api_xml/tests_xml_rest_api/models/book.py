# -*- coding: utf-8 -*-


class Book:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price
