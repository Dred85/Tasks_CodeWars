def get_ages(sum_, difference):
    a = (sum_ + difference) / 2
    b = sum_ - a
    if a - b >= 0 and b >= 0:
        return a, b
    else:
        return None
    # return a,b if a - b > 0 and a > 0 and b >= 0 else None




assert get_ages(24, 4) == (14, 10)

print(get_ages(30, 6))
