def odd_or_even(arr) -> str:
    return "odd" if sum(arr) % 2 == 1 else "even"

print(odd_or_even([0]))
print(odd_or_even([0, 1, 4]))
print(odd_or_even([0, -1, -5]))









    # Input: [0]
    # Output: "even"
    #
    # Input: [0, 1, 4]
    # Output: "odd"
    #
    # Input: [0, -1, -5]
    # Output: "even"