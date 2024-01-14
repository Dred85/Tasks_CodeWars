# def is_it_a_num(s: str) -> str:
#     """
#     Очистка номера телефона от примемей и проверка на количество цифр и начало с 0
#     """
#
#     list_num = [el for el in s if el.isdigit()]
#
#     if len(list_num) == 11 and list_num[0] == '0':
#         return ''.join(list_num)
#
#     return  "Not a phone number"


# второй вариант решения задачи через тернарный оператор
def is_it_a_num(s: str) -> str:
    t = ''.join(i for i in s if i.isdigit())
    return t if len(t)==11 and t[0]=="0" else "Not a phone number"

s = "S:)0207ERGQREG88349F82!efRF)"

print(is_it_a_num(s))