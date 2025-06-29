from typing import List, Tuple
from  collections import Counter

from monkeytype.config import DefaultConfig

# def ordered_count(inp:str) -> List[Tuple[str, int]]:
def ordered_count(inp):
    """ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]"""

    # counter = Counter(inp)
    # seen = set()
    # result = []
    # for char in inp:
    #     if char not in seen:
    #         result.append((char, counter[char]))
    #         seen.add(char)
    # return result

    return list(Counter(inp).items())




if __name__ == "__main__":
    print(ordered_count("abracadabra"))