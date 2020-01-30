# -*- coding: utf-8 -*-


class User:
    def __init__(self, id, name, username, email, address, phone, website, company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_website(self):
        return self.website

    def get_company(self):
        return self.company

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.username == other.username and \
            self.email == other.email and self.address == other.address and self.phone == other.phone and \
            self.website == other.website and self.company == other.company
