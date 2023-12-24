def double_char(s):
    return ''.join([letter*2 for letter in s])

s = "Hello World!"
print(double_char(s))