from abc import ABC,abstractmethod
from collections import *


class Human:

    def __init__(self,name,secindname):
        self.name=name
        self.secindname=secindname

    @abstractmethod
    def work(self):
        return f"{self.name} должен работать не 8 часов , а головой"



class NPC(Human):

    ...



serhiy=NPC("Сергей","Сергеев")
print(serhiy.__dict__)



class Animal(ABC):

    def __init__(self,foot,name):
        self.name=name
        self.foot=foot


    @abstractmethod
    def walk_4(self):
        return f"иду на {self.foot} лапах"

    def walk_2(self):
        return f"иду на {self.foot-2} лапах"


class Dog(Animal):
    ...

dog=Dog("dog",4)



try:
    result = 10 / 0  # Ділення на нуль
except ZeroDivisionError:
    print("Помилка: Ділення на нуль.")


my_list = [1, 2, 3]
try:
    element = my_list[5]  # Доступ до елемента, якого не існує
except IndexError:
    print("Помилка: Неправильний індекс для колекції.")


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Помилка: Ділення на нуль.")
else:
    print(f"Результат: {result}")


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Помилка: Ділення на нуль.")
else:
    print(f"Результат: {result}")
finally:
    print("Цей блок викликається завжди.")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Помилка: Ділення на нуль.")
finally:
    print("Цей блок викликається завжди.")


try:
    value = int("abc")  # Спроба перетворити рядок у число
except ValueError:
    print("Помилка: Не вдалося перетворити рядок у число.")
except TypeError:
    print("Помилка: Неправильний тип даних для перетворення.")
except Exception as e:
    print(f"Інша помилка: {e}")