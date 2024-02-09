def sum_range(start: int, end: int):
    if not isinstance(start, int) or not isinstance(end, int):
        return f"числа должны быть целыми"
    else:
        if start > end:
            start, end = end, start
        return sum([i for i in range(start, end + 1)])


def season(month):
    if 1 <= month <= 12:
        if 3 <= month <= 5:
            return "весна"
        elif 6 <= month <= 8:
            return "літо"
        elif 9 <= month <= 11:
            return "осінь"
        else:
            return "зима"
    else:
        return "Некоректний номер місяця"


def get_filtered(mass: list):
    if not isinstance(mass, list):
        return "Не список"
    return [i for i in mass if i < 5]


def num1(x):
    def num2(y):
        return x * y
    return num2



