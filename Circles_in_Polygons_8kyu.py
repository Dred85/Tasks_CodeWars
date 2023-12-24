import math

def circle_diameter(sides, side_length):
    return side_length / math.tan(math.pi / sides)


print(round(circle_diameter(3, 4), 3))