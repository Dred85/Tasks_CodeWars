# def find_smallest(numbers, to_return):
#     for i in range(len(numbers)):
#         if to_return == 'value':
#             return min(numbers)
#         elif to_return == 'index':
#             if numbers[i] == min(numbers):
#                 return i

def find_smallest(numbers,to_return):
    """Находим минимальный элемент"""
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))



print(find_smallest([5,4,3,2,1],"value"))
print(find_smallest([5,4,3,2,1],"index"))
print(find_smallest([8, 0, 9],"index"))
