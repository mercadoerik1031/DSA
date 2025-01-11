"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, determine the length of its longest substring that consists only of unique characters

Example:
    Input: s = "abcba"
    Output: 3

Explanation:
    Substring "abc" is the longest substring of length 3 that contains unique characters
    ("cba" also fits this description) 
"""


def longest_unique_substring(s: str) -> int:
    if not s:
        return 0

    max_len = 0
    left = right = 0
    seen = set()

    while right < len(s):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        max_len = max(max_len, right - left + 1)
        seen.add(s[right])
        right += 1

    return max_len


# Time Complexity: O(n), Space Complexity: O(1)
