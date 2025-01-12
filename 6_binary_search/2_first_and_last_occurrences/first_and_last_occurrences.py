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
    if not nums:
        return [-1, -1]

    index = binary_search(nums, target)

    if index == -1:
        return [-1, -1]

    left = right = index

    while left >= 0 and nums[left] == nums[index]:
        left -= 1
    left += 1

    while right <= len(nums) - 1 and nums[right] == nums[index]:
        right += 1
    right -= 1

    return [left, right]


def binary_search(arr: List[int], t: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == t:
            return mid

        elif arr[mid] > t:
            right = mid - 1

        else:
            left = mid + 1

    return -1


# Time Complexity: O(n), Space Complexity: O(1)
