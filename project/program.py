from random import random
class MyExeption(Exception):
    pass

class Calculator :

    def __init__(self,varaibesls):
        self.varaibesls = varaibesls
        self.vara=None
        self.varb = None
        try:
            self.vara, self.varb = map(float,self.varaibesls.split(" "))
            if len(self.varaibesls.split(" ")) != 2 :
                raise MyExeption("Операндов не 2 ")
        except Exception as e:
            print("-Ошибка ввода повторите:" , type(e))

    @staticmethod
    def validates(var1, var2):
        try:
            if not isinstance(var1, float) or not isinstance(var2, float):
                raise MyExeption("-Тип данных не число")
            return var1, var2
        except MyExeption as e:
            print(f"-Ошибка ввода: {e}")
            return None, None


    def add(self):
        self.vara, self.varb = self.validates(self.vara, self.varb)
        if self.vara is not None and self.varb is not None:
            return self.vara + self.varb

    def subtract(self):
        self.vara, self.varb = self.validates(self.vara, self.varb)
        if self.vara is not None and self.varb is not None:
            return self.vara - self.varb

    def multiply(self):
        self.vara, self.varb = self.validates(self.vara, self.varb)
        if self.vara is not None and self.varb is not None:
            return self.vara * self.varb

    def divide(self):
        self.vara, self.varb = self.validates(self.vara, self.varb)
        try:
            if self.vara is not None and self.varb is not None:
                return self.vara / self.varb
        except ZeroDivisionError as e:
            print(f"Ошибка деления на ноль: {e}")

    def __str__(self):
        return f"{self.varb} {self.vara}"

