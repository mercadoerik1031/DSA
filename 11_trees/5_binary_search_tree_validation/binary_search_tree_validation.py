"""
Verify whether a binary tree is a valid binary search tree (BST).
A BST is a binary tree where each node meets the following criteria
    - A node's left subtree contains only nodes of lower values than the node's value
    - A nodes's right subtree contains only nodes of greater values than the node's value
"""


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def is_valid_bst(root: TreeNode) -> bool:
    def is_within_bounds(node: TreeNode, lower_bound: int, upper_bound: int) -> bool:
        if not node:
            return True

        if not lower_bound < node.val < upper_bound:
            return False

        if not is_within_bounds(node.left, lower_bound, node.val):
            return False

        return is_within_bounds(node.right, node.val, upper_bound)

    return is_within_bounds(root, float("-inf"), float("inf"))


# Time Complexity = O(n), Space Complexity = O(n)
