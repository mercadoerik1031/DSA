"""
https://leetcode.com/problems/invert-binary-tree/description/

Invert a binary tree and return its root. When a binary tree is inverted,
it becomes the mirror image of itself
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invert_binary_tree(root: TreeNode) -> TreeNode:
    if not root:
        return

    # swap left and right nodes
    root.left, root.right = root.right, root.left

    # recessively invert the left and right subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
