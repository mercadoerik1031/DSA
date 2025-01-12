"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/

A Uniform substring is one in which all character are identical.
Given a string, determine the length of the longest uniform substring that can be formed by replacing 
up to k characters

Example:
    Input: s = "aabcdcca", k = 2
    Output: 5

Explanation:
    If we can only replace 2 characters, the longest uniform substring we can achieve is "ccccc",
    obtained by replace b and d with c
"""


def longest_uniform_substring(s: str, k: int) -> int:
    if k < 0:
        raise ValueError

    counter = {}
    highest_freq = max_len = 0
    left = right = 0

    while right < len(s):
        counter[s[right]] = counter.get(s[right], 0) + 1
        highest_freq = max(highest_freq, counter[s[right]])
        num_chars_to_replace = (right - left + 1) - highest_freq

        if num_chars_to_replace > k:
            counter[s[left]] -= 1
            left += 1

        max_len = right - left + 1

        right += 1

    return max_len


# Time Complexity: O(n), Space Complexity: O(m)
# m = # of unique chars in hash map
