"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string representing an expression of parentheses containing the characters
"(", ")", "{", "}", "[", "]",
determine if the expression form a valid sequence of parentheses.

A sequence of parentheses is valid if every opening parenthesis has a corresponding closing parenthesis,
and no closing parenthesis appears before its matching opening parenthesis.

Example 1:
    Input: s = "([]{})"
    Output: True

Example 2:
    Input: s = "([]{)}"
    Output: False

Explanation:
    The "(" parenthesis is closed before its nested "{" parenthesis is closed
"""

from typing import List


def is_valid_parenthesis(s: List[str]) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for p in s:

        if p in pairs:
            stack.append(p)

        else:
            if stack and pairs[stack[-1]] == p:
                stack.pop()

            else:
                return False

    return not stack


# Time Complexity: O(n), Space: O(n)
