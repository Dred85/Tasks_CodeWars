import math


def degrees(rad):
    return f"{round(rad * 180 / math.pi, 2)}deg"


def radians(deg):
    return f"{round(deg * math.pi / 180, 2)}rad"


math.degrees = degrees
math.radians = radians

print(degrees(1))
print(radians(1))
