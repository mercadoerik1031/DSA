"""
Given an array of intervals, determine the maximum number of intervals that overlap at any point.
Each interval is half-open, meaning it includes the start point but excludes the end point.

Example:
    Input: intervals = [[1, 3], [2, 6], [4, 8], [6, 7], [5, 7]]
    Output: 3

Constraints:
    - The input will contain ar least one interval
    - For every index i in the array. intervals[i].start < intervals[i].end
"""

from typing import List


def largest_overlap(intervals: List[List[int]]) -> int:
    points = []
    for interval in intervals:
        points.append((interval[0], "S"))
        points.append((interval[1], "E"))

    points.sort(key=lambda x: (x[0], x[1]))

    active_overlaps = 0
    max_overlaps = 0
    for _, point_type in points:
        if point_type == "S":
            active_overlaps += 1
        else:
            active_overlaps -= 1

        max_overlaps = max(max_overlaps, active_overlaps)

    return max_overlaps


# Time Complexity O(n log n), Space Complexity O(n)
