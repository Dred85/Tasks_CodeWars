"""
Уникальные подстроки

Дана строка s.
Посчитайте, сколько существует различных пар индексов (i, j) (0≤i≤j<n),
таких что подстрокаs [i..j] не содержит повторяющихся символов,
то есть в ней каждый символ встречается не более одного раза.
Пример 1:

Ввод: aba
Вывод: 5
Пояснение:

i=0: "a"
i=1: "b", "ab"
i=2: "a", "ba"
Пример 2:

Ввод: abc
Вывод: 6
Пояснение:

Подстроки: "a", "b", "c", "ab", "bc", "abc".
"""
def count_unique_substrings(s: str) -> int:
    seen = set()
    left = 0
    total = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        total += right - left + 1

    return total

# Примеры
print(count_unique_substrings("aba"))  # 5
print(count_unique_substrings("abc"))  # 6
