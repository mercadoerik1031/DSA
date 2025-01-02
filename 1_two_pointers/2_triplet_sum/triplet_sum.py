"""
Given an array of integers, return all triplets[a, b, c] such that a + b + c == 0.
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicate triplets).
If no such triplets are found, return an empty array

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
    Input: nums = [0, -1, 2, -3, 1]
    Output: [[-3, 1, 2], [-1, 0, 1]]
"""
from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    """
    Think about a number line with 3 pointers a, b, c
    There is a triplet if a = opposite(b + c) ex a=-3, b=2, c=1
    We have a triplet if -3 = (2 + 1)
    """
    output = []
    nums.sort()  # O(n * log(n))

    for i in range(len(nums)):  # O(n)
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for a
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:  # Worst Case O(n)
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == 0:
                output.append([nums[i], nums[left], nums[right]])

                while (
                    left < right and nums[left] == nums[left + 1]
                ):  # Skip duplicates for b
                    left += 1

                while (
                    right > left and nums[right] == nums[right - 1]
                ):  # Skip duplicates for c
                    right -= 1

                left += 1
                right -= 1

            elif curr_sum > 0:
                right -= 1

            else:
                left += 1

    return output


# Time Complexity: O(n^2), Space Complexity: O(k)
# k = # of triplets
