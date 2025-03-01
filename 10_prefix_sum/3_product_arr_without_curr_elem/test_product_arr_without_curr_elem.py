from product_arr_without_curr_elem import product_without_curr_elem


def test_example_case():
    """Test with the provided example case"""
    nums = [2, 3, 1, 4, 5]
    expected = [60, 40, 120, 30, 24]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_empty_array():
    """Test with an empty array"""
    nums = []
    expected = []
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_single_element():
    """Test with a single element array"""
    nums = [42]
    expected = [1]  # Product of no elements is 1
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_two_elements():
    """Test with two elements"""
    nums = [3, 4]
    expected = [4, 3]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_with_zeros():
    """Test with array containing zeros"""
    nums = [1, 0, 3, 4]
    expected = [0, 12, 0, 0]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_multiple_zeros():
    """Test with array containing multiple zeros"""
    nums = [0, 0, 5, 6]
    expected = [0, 0, 0, 0]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_negative_numbers():
    """Test with negative numbers"""
    nums = [-2, 3, -4, 5]
    expected = [-60, 40, -30, 24]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_all_ones():
    """Test with all elements being 1"""
    nums = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_large_array():
    """Test with a larger array"""
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Calculate expected result manually:
    # For each position, multiply all elements except the one at that position
    expected = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        expected.append(product)

    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"


def test_edge_case_large_numbers():
    """Test with larger numbers to check for overflow issues"""
    nums = [1000, 1000, 1000]
    expected = [1000000, 1000000, 1000000]
    result = product_without_curr_elem(nums)
    assert result == expected, f"Expected {expected} but got {result}"
