import string
import random as e
from collections import OrderedDict
from string import ascii_lowercase as letters
from faker import Faker


class Cars:
    ...


class Expenses:
    ...


class User_generator:
    def __init__(self):
        self.body = {}

    def name(self, key="name", value=None):
        if value is None:
            value = Faker().first_name()
        self.body[key] = value
        return self

    def lastName(self, key="lastName", value=None):
        if value is None:
            value = Faker().last_name()
        self.body[key] = value
        return self

    def email(self, key="email", value=None):
        if value is None:
            value = f"{''.join(e.choice(letters) for _ in range(6))}@gmail.com"
        self.body[key] = value
        return self

    def password(self, key="password", value=None):
        if value is None:
            value = "111wWw111"
        self.body[key] = value
        return self

    def repeatPassword(self, key="repeatPassword", value=None):
        generated_password = None
        if value is None:
            generated_password = self.password().body["password"]
            self.body[key] = generated_password
        self.body[key] = generated_password
        return self

    def dateBirth(self, key="dateBirth", value=None):
        if value is None:
            value = Faker().date()
        self.body[key] = value
        return self

    def country(self, key="country", value=None):
        if value is None:
            value = Faker().country()
        self.body[key] = value
        return self

    def photo(self, key="photo", value=None):
        if value is None:
            value = f"{Faker().first_name()}.jpg"
        self.body[key] = value
        return self

    def user_sign_up_data(self):
        """
        Если нужно словаь уже готовых значений всех для
        :return: dict
        """
        self.name()
        self.lastName()
        self.email()
        self.password()
        self.repeatPassword()
        return self.body

    def bild(self):
        """
        bild
        :return: возвращает созданый словарь
        """
        return self.body

    def user_profile_data(self):
        self.name()
        self.country()
        self.lastName()
        self.dateBirth()
        self.photo()
        return self.body
