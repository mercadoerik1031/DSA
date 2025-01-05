"""
https://leetcode.com/problems/valid-sudoku/submissions/1498796852/

Given a partially completed 9x9 Sudoku board, determine if the current state of the board adheres
to the rules of the game:

Each row and column must contain unique numbers between 1 and 9, or be empty (represented by 0).
Each of the nine 3x3 sub-grid that compose the grid must contain unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the current state of the board is valid given these rules,
not whether the board is solvable.
"""


from typing import List


def is_valid_board(board: List[List[int]]) -> bool:
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    sub_grid_set = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]

            if num == 0:
                continue

            if num < 0 or num > 9:
                return False

            if num in row_set[r]:
                return False

            if num in col_set[c]:
                return False

            if num in sub_grid_set[r // 3][c // 3]:
                return False

            row_set[r].add(num)
            col_set[c].add(num)
            sub_grid_set[r // 3][c // 3].add(num)

    return True


# Time Complexity O(n^2), Space Complexity O(n^2)
