def integrate(coefficient, exponent):
    """Нахождение интеграла"""
    return f'{coefficient//(exponent+1)}x^{exponent+1}'

print(integrate(20, 1))