"""
Пересечение двух массивов
Легкая
Даны два целочисленных массива nums1 и nums2. Верните массив их пересечения.
Каждый элемент в результате должен быть уникальным, а порядок элементов может быть любым.
Пример 1:
Ввод: nums1 = [1,2,2,1], nums2 = [2,2]
Вывод: [2]
Пример 2:
Ввод: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Вывод: [9,4]
Пояснение: [4,9] также принимается.
Ограничения:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
def intersection(nums1: list, nums2:list) -> list:
    set1 = set(nums1)
    set2 = set(nums2)
    set2.add(9)
    res_list = list(set1&set2)
    return res_list

print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))