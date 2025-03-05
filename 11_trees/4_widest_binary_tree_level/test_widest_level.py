from widest_level import TreeNode, widest_level


def test_widest_level():
    # Test 1: Empty tree
    assert widest_level(None) == 0

    # Test 2: Single-node tree
    root = TreeNode(1)
    assert widest_level(root) == 1

    # Test 3: Complete binary tree of depth 3
    """
        Tree Structure:
               1
             /   \
            2     3
           / \   / \
          4   5 6   7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert widest_level(root) == 4  # Level 3 has width = 4 (4, 5, 6, 7)

    # Test 4: Left-skewed tree (each node has only a left child)
    """
        Tree Structure:
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
    assert widest_level(root) == 1  # Only one node per level

    # Test 5: Right-skewed tree (each node has only a right child)
    """
        Tree Structure:
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
    assert widest_level(root) == 1  # Only one node per level

    # Test 6: Tree with missing nodes
    """
        Tree Structure:
              1
             / \
            2   3
           /     \
          4       5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert widest_level(root) == 4
