def sortme(words):
    """Функция сортировки без учета регистра"""

    words = sorted(words, key=str.lower)
    return words


words = ["Hello", "there", "I'm", "fine"]


print(sortme(words))

