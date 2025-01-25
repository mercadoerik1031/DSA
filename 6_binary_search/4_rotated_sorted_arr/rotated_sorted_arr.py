'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

A rotated sorted array is an array of numbers sorted in ascending order, in which a portion
of the array is moved from the beginning to the end. For example, a possible rotation of
[1, 2, 3, 4, 5] is [3, 4, 5, 1, 2], where the first two numbers are moved to the end.

Given a rotated sorted array of unique numbers, return the index of a target value.
If the target value is not present, return -1

Example:
    Input: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
    Output: 2
'''


from typing import List


def rotated_binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # Check if left is sorted
        elif nums[left] <= nums[mid]:
            # if sorted check if target in that range
            if nums[left] <= target < nums[mid]:
                # move right to search left side
                right = mid - 1

            # Else target must be on other side
            else:
                left = mid + 1

        # Check if right is sorted
        elif nums[mid] <= nums[right]:
            # if sorted check if target in that range
            if nums[mid] < target < nums[right]:
                # move left
                left = mid + 1
            
            else:
                # move right
                right = mid - 1

    return -1