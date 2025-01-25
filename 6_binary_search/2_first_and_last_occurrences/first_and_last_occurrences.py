"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers sorted in non-decreasing order, return the first and last indexes of a target number.
if the target is not found return [-1, -1]

Example:
    Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
    Output: [3, 5]

Explanation:
    The first and last occurrences of number 4 are indexes 3 and 5, respectively.
"""

from typing import List


def first_and_last_occurrence(nums: List[int], target: int) -> List[int]:
    def binary_search(is_searching_left: bool = False) -> int:
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                index = mid

                if is_searching_left:
                    right = mid - 1

                else:
                    left = mid + 1

        return index

    left_index = binary_search(True)
    right_index = binary_search(False)

    return [left_index, right_index]


# Time Complexity: O(log n), Space Complexity: O(1)
