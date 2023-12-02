"""Задача с CodeWars"""
def split_into_pairs(string):
    # Если длина строки нечетная, добавляем подчеркивание в конец
    if len(string) % 2 != 0:
        string += '_'

    # Разбиваем строку на пары по два символа
    pairs = [string[i:i+2] for i in range(0, len(string), 2)]

    return pairs

# Пример использования
input_string = input("Введите строку: ")
result = split_into_pairs(input_string)
print(result)