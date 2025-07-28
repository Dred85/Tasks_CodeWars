from collections import Counter


def longest_palindrome(s: str) -> int:
    """"
    Самый длинный палиндром
    Дана строка s, состоящая из строчных или прописных букв. Нужно определить максимальную длину палиндрома, который можно составить из букв этой строки.
Буквы чувствительны к регистру, например, строка "Aa" не считается палиндромом.
Пример 1:
Вход:  s = "abccccdd"
Выход: 7
Пояснение:
Самый длинный палиндром, который можно построить — "dccaccd", его длина равна 7.
Пример 2:
Вход:  s = "a"
Выход: 1"""
    counts = Counter(s)
    length = 0
    has_odd = False

    for count in counts.values():
        length += (count // 2) * 2
        print(length)
        if count % 2 == 1:
            has_odd = True

    if has_odd:
        length += 1

    return length


if __name__ == "__main__":
    print(longest_palindrome("abccccdd"))


