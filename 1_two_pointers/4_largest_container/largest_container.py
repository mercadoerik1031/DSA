"""
You are given a array of numbers, each representing the height of a vertical line on a graph.
A container can be formed with any pair of these lines, along with the x-axis of the graph.
Return the amount of water which the largest container can hold

Example:
    Input: heights = [2, 7, 8, 3, 7, 6]
    Output: 24
"""


from typing import List


def largest_container(heights: List[int]) -> int:
    if len(heights) < 2:  # Need at least 2 lines to form a container
        return 0

    left, right = 0, len(heights) - 1
    area = 0

    while left < right:
        length = right - left
        height = min(
            max(0, heights[left]), max(0, heights[right])  # Handle negative heights
        )
        curr_area = height * length
        area = max(area, curr_area)

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return area


# Time Complexity O(n), Space Complexity O(1)
