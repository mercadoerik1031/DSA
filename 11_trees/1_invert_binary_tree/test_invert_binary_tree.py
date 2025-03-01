from invert_binary_tree import TreeNode, invert_binary_tree


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
    assert invert_binary_tree(None) is None

    # Test single node tree
    root = TreeNode(1)
    assert tree_to_list(invert_binary_tree(root)) == [1]

    # Test small binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    inverted = invert_binary_tree(root)
    assert tree_to_list(inverted) == [1, 3, 2]

    # Test larger binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    inverted = invert_binary_tree(root)
    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]
