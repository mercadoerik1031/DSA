"""
https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
"""

from typing import List


def numberOfAlternatingGroups(colors: List[int], k: int) -> int:
    res = 0
    left, right = 0, 1

    # Expand colors to handle circular
    colors.extend(colors[:k-1])

    while right < len(colors):
        # Check if curr color is the same as the last one
        if colors[right] == colors[right - 1]:
            # Pattern breaks, reset window from curr position
            left = right
            right += 1
            continue
        
        # Expand window
        right += 1

        # Skip counting sequence if its length is less than k
        if right - left < k:
            continue
        
        # Record a valid sequence and shrink window from left
        res += 1
        left += 1

    return res


colors = [0, 1, 0, 1, 0]
k = 3
print(numberOfAlternatingGroups(colors, k))
