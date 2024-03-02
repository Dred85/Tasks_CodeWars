def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True



# def is_palindrome(s):
#     s = s.lower().replace(" ", "")  # Преобразуем строку в нижний регистр и удаляем пробелы
#     for i in range(len(s) // 2):  # Проходим только до середины строки
#         if s[i] != s[len(s) - i - 1]:  # Сравниваем символы с обоих концов строки
#             return False
#     return True




print(is_palindrome('ABCA'))
