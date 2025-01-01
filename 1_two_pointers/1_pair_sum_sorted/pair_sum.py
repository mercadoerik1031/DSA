'''
Given an array of integers sorted in ascending order and a target value, return the indexes
of any pair of numbers in the array that sum to the target.

The order of the indexes in the result doesn't matter. If you pair is found return an empty array.
'''

from typing import List

def pair_sum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        
        elif curr_sum > target:
            right -= 1
        
        else:
            left += 1
            
    return []

# Time Complexity: O(n), Space Complexity O(1)