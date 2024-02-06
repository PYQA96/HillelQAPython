import string
import random as e
from collections import OrderedDict
from string import ascii_lowercase as letters
from faker import Faker


class Cars:
    ...


class Expenses:
    ...

class InsideMethod:

    def __init__(self,params):
        self.faker = Faker()
        self.params=params
        self.body = {self.params : self.faker.first_name()}

    def bild(self):
        return self.body

class User_generator:
    def __init__(self):
        self.body = {}
        self.faker =Faker()

    def name(self, value=None):
        if value is None:
            value = self.faker.first_name()
        self.body["name"] = value
        return self

    def last_Name(self, value=None):
        if value is None:
            value = Faker().last_name()
        self.body["lastName"] = value
        return self

    def email(self, value=None):
        if value is None:
            value = f"{''.join(e.choice(letters) for _ in range(6))}@gmail.com"
        self.body["email"] = value
        return self

    def password(self, value=None):
        if value is None:
            value = "111wWw111"
        self.body["password"] = value
        return self

    def repeat_Password(self, value=None):
        generated_password = None
        if value is None:
            generated_password = self.password().body["password"]
            self.body["repeatPassword"] = generated_password
        self.body["repeatPassword"] = generated_password
        return self

    def date_Birth(self, value=None):
        if value is None:
            value = self.faker.date()
        self.body["dateBirth"] = value
        return self

    def country(self, value=None):
        if value is None:
            value = self.faker.country()
        self.body["country"] = value
        return self

    def photo(self, value=None):
        if value is None:
            value = f"{Faker().first_name()}.jpg"
        self.body["photo"] = value
        return self

    def user_sign_up_data(self):
        self.name()
        self.last_Name()
        self.email()
        self.password()
        self.repeat_Password()
        return self.body

    def user_profile_data(self):
        self.name()
        self.country()
        self.last_Name()
        self.date_Birth()
        self.photo()
        return self.body

    def attached_data(self, key, value):
        if isinstance(key,str):
            self.body[key]=InsideMethod(value).bild()
        else:
            temp = self.body
            for k in key[:-1]:
                if k not in temp.keys():
                    temp[k] = {}
                    temp=temp[k]
            temp[key[-1]]=InsideMethod(value).bild()
        return self


    def cusstom_bild(self):
        return self.body



