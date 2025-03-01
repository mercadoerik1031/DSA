"""
Find the number of sub-arrays in an integer array that sum to k.

Example:
    Input: nums = [1, 2, -1, 1, 2], k = 3
    Output = 3 ([1, 2], [1, 2, -1, 1], [1, 2])
"""

from typing import List


def k_sum_subarrays(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]

        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count


# Time Complexity: O(n), Space Complexity: O(n)


# def k_sum_subarrays(nums: List[int], k: int) -> int:
#     n = len(nums)
#     count = 0
#     prefix_sum = [0]

#     for i in range(n):
#         prefix_sum.append(prefix_sum[-1] + nums[i])

#     for j in range(1, n + 1):
#         for i in range(1, j + 1):
#             if prefix_sum[j] - prefix_sum[i - 1] == k:
#                 count += 1

#     return count


# Time Complexity: O(n^2), Space Complexity: O(n)


# def k_sum_subarrays(nums: List[int], k: int) -> int:
#     n = len(nums)
#     count = 0

#     for start in range(n):
#         curr_sum = 0

#         for end in range(start, n):
#             curr_sum += nums[end]
#             if curr_sum == k:
#                 count += 1

#     return count


# Time Complexity: O(n^2), Space Complexity: O(1)
