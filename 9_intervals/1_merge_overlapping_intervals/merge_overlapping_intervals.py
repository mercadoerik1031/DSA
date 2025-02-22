"""
https://leetcode.com/problems/merge-intervals/description/

Merge an array of intervals so there are no overlapping intervals, and return the resultant merged intervals.

Example:
    Input: intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
    Output: [[1,5], [6,8]]

Constraints:
    - The input contains at least one interval
    - For every index i in the array, intervals[i].start <= intervals[i].end
"""

"""
TIP:
    if a.end < b.start: intervals are NOT overlapping
    if a.end >= b.start: intervals are overlapping
"""


from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for B_interval in intervals[1:]:
        A_interval = merged[-1]

        if A_interval[1] < B_interval[0]:
            merged.append(B_interval)

        else:
            merged[-1][1] = max(A_interval[1], B_interval[1])

    return merged


# Time Complexity: O(n log n), Space Complexity: O(n)
