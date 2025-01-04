"""
Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result doesn't matter.
If no pair is found, return an empty array

Example:
    Input: nums = [-1, 3, 4, 2], target = 3
    Output: [0, 2]

Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
    The same index cannot be used twice in the result
"""


from typing import List


def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    dic = {}

    for i in range(len(nums)):
        compliment = target - nums[i]
        
        if compliment in dic:
            return [i, dic[compliment]]

        dic[nums[i]] = i

    return []


# Time Complexity O(n), Space Complexity O(n)
