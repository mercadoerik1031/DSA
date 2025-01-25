"""
You are given an array representing the heights of trees,
and an integer k representing the total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain heigh, H.
The machine cuts off the top part of all trees taller than H, while trees shorter than H remain untouched.
Determine the highest possible setting of the wood cutter (H) so that it cuts at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest tree in the array.

Example:
    Input: heights = [2, 6, 3, 8], k = 7
    Output: 3

Explanation:
    The highest possible height setting that yields at least k = 7 meters of wood is 3,
    which yields 8 meters of wood. Any heigh setting higher than this will yield less than 7
    meters of wood.

Constraints:
    It's always possible to attain at least k meters of wood.
    There's at least one tree.
"""

from typing import List


def find_height(k: int, heights: List[int]) -> int:
    def cuts_enough_wood(machine_height: int):
        wood_cut = 0

        for wood_height in heights:
            if wood_height > machine_height:
                wood_cut += wood_height - machine_height

        return wood_cut >= k

    left, right = 0, max(heights)

    while left < right:
        mid = (left + right) // 2 + 1 # + 1 for upper bound search

        if cuts_enough_wood(mid):
            left = mid

        else:
            right = mid - 1

    return right
