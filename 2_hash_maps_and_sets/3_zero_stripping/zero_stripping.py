"""
https://leetcode.com/problems/set-matrix-zeroes/description/

For each zero in a m x n matrix, set its entire column to zero in place:
"""


from typing import List


def zero_stripping(matrix: List[List[int]]) -> None:
    rows, cols = set(), set()
    r, c = len(matrix), len(matrix[0])

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    print(f"Rows: {rows}, Columns: {cols}")

    for i in range(r):
        for j in range(c):
            if i in rows or j in cols:
                matrix[i][j] = 0


# Time Complexity: O(row * col), Space Complexity: O(row + col)
