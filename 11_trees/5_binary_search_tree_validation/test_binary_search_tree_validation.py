from binary_search_tree_validation import TreeNode, is_valid_bst


class TestValidBST:
    def test_empty_tree(self):
        """Test that an empty tree is a valid BST."""
        assert is_valid_bst(None) == True

    def test_single_node(self):
        """Test that a single node is a valid BST."""
        root = TreeNode(10)
        assert is_valid_bst(root) == True

    def test_valid_bst_simple(self):
        """Test a simple valid BST with three nodes."""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        assert is_valid_bst(root) == True

    def test_valid_bst_complex(self):
        """Test a more complex valid BST."""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(20)
        assert is_valid_bst(root) == True

    def test_invalid_bst_left_subtree(self):
        """Test a tree that is invalid because of a value in the left subtree."""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        # This value is greater than the root node, violating BST property
        root.left.right = TreeNode(12)
        assert is_valid_bst(root) == False

    def test_invalid_bst_right_subtree(self):
        """Test a tree that is invalid because of a value in the right subtree."""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        # This value is less than the root node, violating BST property
        root.right.left = TreeNode(8)
        assert is_valid_bst(root) == False

    def test_invalid_bst_equal_value(self):
        """Test a tree that is invalid because of equal values."""
        root = TreeNode(10)
        root.left = TreeNode(10)  # Same value as parent, should be invalid
        assert is_valid_bst(root) == False

    def test_valid_bst_with_negative_values(self):
        """Test a valid BST with negative values."""
        root = TreeNode(0)
        root.left = TreeNode(-10)
        root.right = TreeNode(10)
        root.left.left = TreeNode(-20)
        root.left.right = TreeNode(-5)
        assert is_valid_bst(root) == True

    def test_deep_right_violation(self):
        """Test a tree with a violation deep in the right branch."""
        root = TreeNode(50)
        root.left = TreeNode(30)
        root.right = TreeNode(80)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(90)
        # This node violates the BST property because it's less than 50
        root.right.right.left = TreeNode(40)
        assert is_valid_bst(root) == False

    def test_deep_left_violation(self):
        """Test a tree with a violation deep in the left branch."""
        root = TreeNode(50)
        root.left = TreeNode(30)
        root.right = TreeNode(80)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(40)
        # This node violates the BST property because it's greater than 50
        root.left.left.right = TreeNode(60)
        assert is_valid_bst(root) == False

    def test_edge_case_min_max_values(self):
        """Test with values at the extremes of the integer range."""
        root = TreeNode(0)
        root.left = TreeNode(-2147483648)  # Min 32-bit integer
        root.right = TreeNode(2147483647)  # Max 32-bit integer
        assert is_valid_bst(root) == True

    def test_skewed_left_tree(self):
        """Test a valid left-skewed BST."""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(2)
        root.left.left.left.left = TreeNode(1)
        assert is_valid_bst(root) == True

    def test_skewed_right_tree(self):
        """Test a valid right-skewed BST."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        assert is_valid_bst(root) == True
