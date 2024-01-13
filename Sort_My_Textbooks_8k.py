def sorter(textbooks):
    return sorted(textbooks, key=str.lower)

print(sorter(['f', 'T', 'A']))