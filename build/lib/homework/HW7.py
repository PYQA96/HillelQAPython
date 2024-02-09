import random
from collections import Counter
from collections import ChainMap
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
from random import randint

# 1 cсоздание коллекции для Counter
String_to_perfomance = "".join([random.choice("0123456789") for i in range(9)])
String_to_perfomance = {int(key): value for key, value in Counter(String_to_perfomance).items()}


def count_it(sequence):
    return Counter(sequence).most_common(3)


def count_max_value(sequence):
    sequence = sorted(sequence.items(), key=lambda x: x[1])
    return sequence[:3]


print(f"Изначальный словарь {String_to_perfomance}")
print(f"3 самых частых {count_it(String_to_perfomance)}")
print(f"3 самых нечастых {count_max_value(String_to_perfomance)}")

# 2 namedtuple: Створити namedtuple з іменем Fish та іменними аргументами "name", "species",
# "tank". Створити кілька об'єктів такого namedtuple. Вибрати один з них та за допомогою вбудованої функції _asdict()
# вивести його як словник у консоль.


Fish = namedtuple("Fish", ["name", "species", "tank"])
seledka = Fish('seledka', 'species', 'tank')
okun = Fish('okun', 'species_okun', 'tank_okun')
print(seledka)
print(okun)
okun = okun._replace(name="Ne_okun")
seledka = seledka._replace(name="Ne_seledka")
print(okun)
print(okun._asdict())
print(seledka._asdict())
a = okun._asdict()

# 3defaultdict: Використовуючи один з варіантів namedtuple
# створити defaultdict та задати йому відповідний тип даних
# (Згідно тому що маємо в namedtuple) для значень за замовчуванням.

def_dict=defaultdict(None,a)
print(def_dict)


#4 deque: Створити відповідний пустий список deque,
# та показати як легко додати на початок, на кінець списку не використовуючи індексів,
# а також як легко видалити з обох кінців.


deque=OrderedDict({list(i for i in range(1,11))[i]:random.choice("123456789") for i in range(10)})
print(deque)
deque.move_to_end(1,last=True)
print(deque)
deque.move_to_end(2,last=True)
print(deque)
deque.popitem(last=True)
print(deque)
deque.popitem(last=False)
print(deque)



#5 Декоратор





import random


def decorator(function):
    number1=random.randint(1,100)
    number2 = random.randint(1, 100)
    def warper(*args):
        function(*args)

        print("Вызвали сумму рандомных чисел")
        print(f"Сумма чисел = {sum(args)+number2+number1}")
        return f"Сумма числе функции переданой в декоратор {sum(args)}"

    return warper

@decorator
def my_fuc(a,b):
    return a+b


print(my_fuc(1,2))








