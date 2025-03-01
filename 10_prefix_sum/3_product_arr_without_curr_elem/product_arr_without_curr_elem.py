"""
https://leetcode.com/problems/product-of-array-except-self/description/

Given an array of integers, return an array res so that res[i] is equal to the product
of all the elements of the input array except nums[i] itself.

Example:
    Input: nums = [2, 3, 1, 4, 5]
    Output: [60, 40, 120, 30, 24]

Explanation: The output value at index 0 is the product of all numbers except nums[0]
(3 * 1 * 4 * 5). The same logic applies to the rest of the output
"""

from typing import List


def product_without_curr_elem(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]

    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]

    return res


# Time Complexity: O(n), Space Complexity: O(1)


# def product_without_curr_elem(nums: List[int]) -> List[int]:
#     n = len(nums)
#     product = 1

#     for i in range(n):
#         product *= nums[i]

#     res = [product] * n

#     for i in range(n):
#         res[i] = res[i] // nums[i]

#     return res


# Time Complexity: O(n), Space Complexity: O(n)


# def product_without_curr_elem(nums: List[int]) -> List[int]:
#     n = len(nums)
#     products = []

#     for i in range(n):
#         product = 1
#         for j in range(n):
#             if i == j:
#                 continue
#             else:
#                 product *= nums[j]
#         products.append(product)

#     return products


# Time Complexity: O(n^2), Space Complexity: O(n)

nums = [2, 3, 1, 4, 5]
print(product_without_curr_elem(nums))
