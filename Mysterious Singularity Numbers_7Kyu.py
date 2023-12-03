def real_numbers(n):
    """ Ищем количество натуральных чисел в
    коллекции из n чисел не делящихся ни на одно из чисел [2, 3, 5]"""

    # return len([num for num in range(1, n + 1) if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0)])
    return n - n//2 - n//3 - n//5 + n//6 + n//10 + n//15 - n//30
print(real_numbers(100))

