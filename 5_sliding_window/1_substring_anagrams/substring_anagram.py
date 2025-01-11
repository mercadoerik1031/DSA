"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given two strings, s and t, both consisting of lowercase English letters, return the number of 
substrings in s that are anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
using all the original letters exactly once

Example:
    Input: s = "caabab", t = "aba"
    Output: 2
    
Explanation:
    There is an anagram of t starting at index 1 ("aab") and another starting at index 2 ("aba").
"""


def count_substring_anagram(s: str, t: str) -> int:
    if not t or len(t) > len(s):
        return 0

    t_freqs, window_freqs = [0] * 26, [0] * 26
    counter = 0

    # Count frequencies in 't'
    for char in t:
        t_freqs[ord(char) - ord("a")] += 1

    left = right = 0

    while right < len(s):
        window_freqs[ord(s[right]) - ord("a")] += 1

        # Check length of window
        if right - left + 1 == len(t):
            if t_freqs == window_freqs:
                counter += 1

            # Slide window
            window_freqs[ord(s[left]) - ord("a")] -= 1
            left += 1

        right += 1

    return counter


# Time Complexity: O(n), Space Complexity O(1)
