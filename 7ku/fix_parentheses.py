"""Input: ")("
Output: "()()"

Input: "))))(()("
Output: "(((())))(()())"""

def fix_parentheses(stg):
    original, o, c = stg, "(", ")"
    while "()" in stg:
        stg = stg.replace("()", "")
    opening, closing = o * stg.count(c), c * stg.count(o)
    return f"{opening}{original}{closing}"




if __name__ == "__main__":
    print(fix_parentheses(")("))
    print(fix_parentheses("(((())))(()())"))