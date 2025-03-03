"""
https://leetcode.com/problems/balanced-binary-tree/description/

Determine if a binary tree is height-balanced, meaning no node's left subtree and right subtree have a height difference greater than 1
"""


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def is_balanced(root: TreeNode) -> bool:
    def get_height(node: TreeNode) -> int:
        if not node:
            return 0

        left_height = get_height(node.left)
        right_height = get_height(node.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return get_height(root) != -1


# Time Complexity: O(n), Space Complexity: O(n)
