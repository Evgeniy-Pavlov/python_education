"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x ** 2 for x in list(args)]

def is_prime(x):
    if x in (0, 1):
        return False
    else:
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return False
        return True

# filter types
ODD = lambda x: x % 2 == 1
EVEN = lambda x: x % 2 == 0
PRIME = is_prime


def filter_numbers(list_num, arg):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    return list(filter(arg, list_num))