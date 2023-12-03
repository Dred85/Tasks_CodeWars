def quadratic(x1, x2):
    """ коэффициенты квадратного уравнения"""
    a = 1
    b = -(x1 + x2)
    c = x1*x2

    return (a, b, c)

print(quadratic(4,9))