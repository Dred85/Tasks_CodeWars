def triple_trouble(one, two, three):
    res = ''
    for i in range(len(one)):
        result = one[i] + two[i] + three[i]
        res += result
    return res


one, two, three = "aaaaaa","bbbbbb","cccccc"
print(triple_trouble(one, two, three))

# def triple_trouble(one, two, three):
#     return ''.join(''.join(a) for a in zip(one, two, three))
#
# one, two, three = "aaa","bbb","ccc"
# print(triple_trouble(one, two, three))