from right_most_node import get_right_most, TreeNode


def test_empty_tree():
    assert get_right_most(None) == []


def test_single_node():
    root = TreeNode(1)
    assert get_right_most(root) == [1]


def test_balanced_tree():
    """
    Tree structure:
          1
         / \
        2   3
       / \   \
      4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    assert get_right_most(root) == [1, 3, 6]


def test_unbalanced_tree():
    """
    Tree structure:
          1
           \
            2
             \
              3
               \
                4
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    assert get_right_most(root) == [1, 2, 3, 4]


def test_left_skewed_tree():
    """
    Tree structure:
          1
         /
        2
       /
      3
     /
    4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)

    assert get_right_most(root) == [1, 2, 3, 4]


def test_mixed_tree():
    """
    Tree structure:
          1
         / \
        2   3
       /   / \
      4   5   6
         /
        7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)

    assert get_right_most(root) == [1, 3, 6, 7]
