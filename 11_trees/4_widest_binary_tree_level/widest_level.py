"""
https://leetcode.com/problems/maximum-width-of-binary-tree/description/

Return the width of the widest level in a binary tree, where the width of a level is
defined as the distance between its leftmost and rightmost non-null nodes
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


def widest_level(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([(root, 0)])
    max_width = 0

    while queue:
        _, left = queue[0]
        _, right = queue[-1]
        max_width = max(max_width, right - left + 1)

        for _ in range(len(queue)):
            node, idx = queue.popleft()

            if node.left:
                queue.append((node.left, idx * 2))

            if node.right:
                queue.append((node.right, idx * 2 + 1))

    return max_width


# Time Complexity: O(n), Space Complexity: O(n)
