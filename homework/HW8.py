# Lambda

# Лямбда функція, яка друкує символ переданий як перший аргумент ту кількість раз, яка вказана в другому аргументі (за замовчуванням 100).
print_char = lambda char, times=100: print(char * times)



# Лямбда функція, яка приймає два числа і повертає більше з них, використовуючи тернарний if.
get_max = lambda a, b: a if a > b else b


# Лямбда функція, яка завжди повертає 10.
always_10 = lambda: 10



# List comprehension

# Додавання 6 до кожного елемента у lst1 за допомогою list comprehension.
lst1 = [44, 54, 64, 74, 104]
lst2 = [x + 6 for x in lst1]



# Піднесення кожного елемента у lst3 до квадрату за допомогою list comprehension.
lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [x ** 2 for x in lst3]



# Виділення назв транспортних засобів вагою до 5000 кілограмів та перетворення їх на великі літери.
car_dict = {
    "Sedan": 1500,
    "SUV": 2000,
    "Pickup": 2500,
    "Minivan": 1600,
    "Van": 2400,
    "Semi": 13600,
    "Bicycle": 7,
    "Motorcycle": 110
}

list5 = [key.upper() for key, value in car_dict.items() if value <= 5000]
# или
list5 = {key : value for key,value in car_dict.items() if value <= 5000 }
print(list5)
# или
list5 = [*{key : value for key,value in car_dict.items() if value <= 5000 }]
print(list5)



# Map

# Функція, яка повертає назву місяця за його номером.
def get_month_name(month_number):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return months[month_number - 1]


months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


month_names = list(map(get_month_name, months_list))


