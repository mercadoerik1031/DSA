from invert_binary_tree import (
    TreeNode,
    invert_binary_tree_recursive,
    invert_binary_tree_iteratively,
)


def tree_to_list(root):
    """Helper function to convert a binary tree to a list (level-order traversal)."""
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()  # Remove trailing None values
    return result


def test_invert_binary_tree():
    # Test empty tree
    assert invert_binary_tree_recursive(None) is None
    assert invert_binary_tree_iteratively(None) is None

    # Test single node tree
    root = TreeNode(1)
    assert tree_to_list(invert_binary_tree_recursive(root)) == [1]
    assert tree_to_list(invert_binary_tree_iteratively(root)) == [1]

    # Test small binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    inverted_rec = invert_binary_tree_recursive(root)
    assert tree_to_list(inverted_rec) == [1, 3, 2]

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    inverted_iter = invert_binary_tree_iteratively(root1)
    assert tree_to_list(inverted_iter) == [1, 3, 2]

    # Test larger binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    inverted_rec = invert_binary_tree_recursive(root)
    assert tree_to_list(inverted_rec) == [4, 7, 2, 9, 6, 3, 1]

    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    inverted_iter = invert_binary_tree_iteratively(root1)
    assert tree_to_list(inverted_iter) == [4, 7, 2, 9, 6, 3, 1]
