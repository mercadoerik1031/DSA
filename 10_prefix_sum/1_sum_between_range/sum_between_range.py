"""
https://leetcode.com/problems/range-sum-query-immutable/description/

Given an integer array, write a function which returns the sum of values
between two indexes

Example:
    Input: arr = [3, -7, 6, 0, -2, 5] idx1 = 0, idx2 = 3
    Output: 2

    Input: arr = [3, -7, 6, 0, -2, 5] idx1 = 2, idx2 = 4
    Output: 4

    Input: arr = [3, -7, 6, 0, -2, 5] idx1 = 2, idx2 = 2
    Output: 6

    Input: arr = [3, -7, 6, 0, -2, 5] [sum_range(0, 3), sum_range(2, 4), sum_range(2, 2)]
    Output: [2, 4, 6]
"""

from typing import List


def sum_range(arr: List[int], idx1: int, idx2: int) -> int:
    # Edge Case: arr is empty
    if not arr:
        raise IndexError

    n = len(arr)

    # Edge Case: Convert negative index to positive index
    if idx1 < 0:
        idx1 = n + idx1
    if idx2 < 0:
        idx2 = n + idx2

    # Edge Case: index is out of bounds
    if idx1 < 0 or idx1 >= n or idx2 < 0 or idx2 >= n:
        raise IndexError

    # Edge Case: first index larger than second
    if idx1 > idx2:
        raise ValueError

    prefix_sum = [0] * n

    for i in range(n):
        if i > 0:
            prefix_sum[i] = prefix_sum[i - 1] + arr[i]
        else:
            prefix_sum[i] = arr[i]

    return prefix_sum[idx2] - prefix_sum[idx1 - 1] if idx1 > 0 else prefix_sum[idx2]


# Time Complexity: O(n), Space Complexity: O(1)
