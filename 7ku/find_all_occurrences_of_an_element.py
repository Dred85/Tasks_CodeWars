from typing import List

def find_all(array: list[int], n: int) -> list[int]:
    """find_all([6, 9, 3, 4, 3, 82, 11], 3)
> [2, 4]"""
    # res_list =[]
    # for i, v in enumerate(array):
    #     if v == n:
    #         res_list.append(i)
    # return res_list

    return [i for i, v in enumerate(array) if v == n]


if __name__ == "__main__":
    print(find_all([6, 9, 3, 4, 3, 82, 11], 3))
