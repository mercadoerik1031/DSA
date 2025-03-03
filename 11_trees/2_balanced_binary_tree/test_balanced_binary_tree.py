from balanced_binary_tree import TreeNode, is_balanced


def test_empty_tree():
    assert is_balanced(None) is True


def test_single_node():
    root = TreeNode(1)
    assert is_balanced(root) is True


def test_balanced_tree_simple():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert is_balanced(root) is True


def test_unbalanced_tree_simple():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert is_balanced(root) is False


def test_balanced_tree_deeper():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert is_balanced(root) is True


def test_unbalanced_tree_deeper():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    assert is_balanced(root) is False


def test_unbalanced_right_side():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert is_balanced(root) is False


def test_unbalanced_uneven_beyond_limit():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    root.right = TreeNode(3)
    assert is_balanced(root) is False
