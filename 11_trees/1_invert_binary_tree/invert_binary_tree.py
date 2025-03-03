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


def invert_binary_tree_recursive(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # swap left and right nodes
    root.left, root.right = root.right, root.left

    # recessively invert the left and right subtrees
    invert_binary_tree_recursive(root.left)
    invert_binary_tree_recursive(root.right)

    return root


# Time Complexity: O(n), Space Complexity: O(1)


def invert_binary_tree_iteratively(root: TreeNode) -> TreeNode:
    if not root:
        return None

    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return root


# Time Complexity: O(n), Space Complexity: O(n)
