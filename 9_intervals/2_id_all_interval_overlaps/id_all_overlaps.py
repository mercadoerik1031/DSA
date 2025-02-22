"""
https://leetcode.com/problems/interval-list-intersections/description/

Return an array of all overlaps between two arrays of intervals;
intervals1 and intervals2. Each individual interval array is sorted by start value,
and contains no overlapping intervals within itself.

Example:
    Input: intervals1 = [[1, 4], [5, 6], [9, 10]], intervals2 = [[2, 7], [8, 9]]
    Output: [[2, 4], [5, 6], [9, 9]]

Constraints:
    - For every index i in intervals1, intervals1[i].start < intervals1[i].end
    - For every index j in intervals2, intervals2[j].start < intervals2[j].end
"""


from typing import List


def id_all_overlaps(
    intervals1: List[List[int]], intervals2: List[List[int]]
) -> List[List[int]]:
    overlap = []
    i = j = 0

    while i < len(intervals1) and j < len(intervals2):
        start = max(intervals1[i][0], intervals2[j][0])
        end = min(intervals1[i][1], intervals2[j][1])

        if start <= end:
            overlap.append([start, end])

        if intervals1[i][1] < intervals2[j][1]:
            i += 1
        else:
            j += 1

    return overlap


# Time Complexity: O(n + m), Space Complexity: O(1)
