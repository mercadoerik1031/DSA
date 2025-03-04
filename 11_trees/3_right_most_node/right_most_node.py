"""
https://leetcode.com/problems/binary-tree-right-side-view/description/

Return an array containing the values of the right most nodes at each level of a binary tree
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


def get_right_most(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if i == level_size - 1:
                res.append(node.val)

    return res


# Time Complexity: O(n), Space Complexity: O(n)
