"""
A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after remove all non-alphanumeric characters.
A character is alphanumeric if it's either a letter or a number.

Example 1:
    Input: s = "a dog! a panic in a pagoda."
    Output: True
    
Example 2:
    Input: s = "abc123"
    Output: False
    
Constraints:
    The string may include a combination of lowercase English letters, numbers, spaces, and punctuations.
"""


def clean_string(s: str) -> str:
    """
    Removes non-alphanumeric characters
    """
    output = ""

    for char in s:
        if char.isalnum():
            output += char

    return output


def is_valid_palindrome(s: str) -> bool:
    s = clean_string(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


# Time Complexity O(n), Space Complexity O(n)


def is_valid_palindrome_optimized(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while right > left and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


# Time Complexity O(n), Space Complexity O(1)
