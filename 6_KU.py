#Задача с codewars 6 кю
def sortme(words: str) ->list :
    """Функция сортировки без учета регистра"""

    words = sorted(words, key=str.lower)

    return words


words = ["Hello", "there", "I'm", "fine"]
print(sortme(words))

