def is_correct_bracket_sequence(sequence):
    """ Подсчет открытых и закрытых скобок """

    count = 0 # ввели счетчик скобок
    for char in sequence: #запускаем цикл
        count = count + 1 if char == '(' else count - 1 # условие, если скобка открытв "(" прибавляем +1 к счетчика, если скобка закрыта ) -1
        if count < 0:
            return False

    return count == 0

print(is_correct_bracket_sequence(input()))