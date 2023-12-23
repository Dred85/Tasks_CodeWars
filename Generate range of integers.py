def generate_range(start, stop, step):
    return list(i for i in range(start, stop + 1, step))


print(generate_range(1, 15, 20))