def contains_duplicate(nums:list[int]) -> bool:
    """Поиск дубликатов
Дан целочисленный массив nums, верните true, если какое-либо значение встречается в массиве хотя бы дважды, и верните false, если все элементы уникальны.
Пример 1:
Ввод: nums = [1,2,3,1]
Вывод: true
Объяснение: Элемент 1 встречается на индексах 0 и 3.
Пример 2:
Ввод: nums = [1,2,3,4]
Вывод: false
Объяснение: Все элементы уникальны.
Пример 3:
Ввод: nums = [1,1,1,3,3,4,3,2,4,2]
Вывод: true"""
    # return True if list(set(nums)) != nums else False
    return len(nums) != len(set(nums))

if __name__ == '__main__':
    print(contains_duplicate([1,2,3,1]))
    print(contains_duplicate([1,2,3,4]))
    print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
    print(contains_duplicate([3, 1]))