
"""
Последовательные символы
Мощность строки — это максимальная длина непустой подстроки, содержащей только один уникальный символ.
Требуется вернуть мощность строки s.
Пример 1:
Ввод: s = "meet"
Вывод: 2
Пояснение: подстрока "ee" длины 2 содержит только символ "e".
Пример 2:
Ввод: s = "abbcccddddeeeeedcba"
Вывод: 5
Пояснение: подстрока "eeeee" длины 5 содержит только символ "e".
Ограничения:
"""


def max_power(s: str) -> int:
    max_len = 1
    current_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len

print(max_power("abbcccddddeeeeedcba"))
print(max_power("tourist"))
print(max_power("meet"))
