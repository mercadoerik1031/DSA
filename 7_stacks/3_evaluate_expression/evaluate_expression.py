"""
Given a string representing a mathematical expression containing integers,
parentheses, addition, and subtraction operators, evaluate and return the result of the expression.

Example:
    Input: s = "18-(7+(2-4))"
    Output: 13
"""


def evaluate_expression(s: str) -> int:
    stack = []
    curr_num, sign, res = 0, 1, 0

    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)

        elif c == "-" or c == "+":
            res += curr_num * sign
            sign = -1 if c == "-" else 1
            curr_num = 0

        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1

        elif c == ")":
            res += sign * curr_num
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0

    return res + curr_num * sign


# Time Complexity: O(n), Space Complexity: O(n)
