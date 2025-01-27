"""
Given an integer array nums, return an output array res where, for each value nums[i],
res[i] is the first number to the right that's larger than nums[i].
If no larger number exists to the right of nums[i], set ses[i] to -1

Example 1:
    Input: nums = [5, 2, 4, 6, 1]
    Output: [6, 4, 6, -1, -1]
"""

from typing import List


def largest_number_to_right(nums: List[int]) -> List[int]:
    n = len(nums)
    stack = []
    res = [0] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res


# Time Complexity: O(n), Space Complexity: O(1)
