from k_sum_subarrays import k_sum_subarrays


def test_example_case():
    """Test with the provided example case"""
    nums = [1, 2, -1, 1, 2]
    k = 3
    expected = 3
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_empty_array():
    """Test with an empty array"""
    nums = []
    k = 5
    expected = 0
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_single_element_equal_to_k():
    """Test with a single element equal to k"""
    nums = [3]
    k = 3
    expected = 1
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_single_element_not_equal_to_k():
    """Test with a single element not equal to k"""
    nums = [5]
    k = 3
    expected = 0
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_all_zeros():
    """Test with an array of all zeros and k=0"""
    nums = [0, 0, 0, 0]
    k = 0
    # Every subarray of continuous zeros sums to 0
    # There are n*(n+1)/2 = 4*5/2 = 10 total subarrays
    expected = 10
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_negative_numbers():
    """Test with negative numbers"""
    nums = [-1, 2, -3, 4, -5]
    k = -1
    # Subarrays that sum to -1: [-1], [2, -3], [4, -5]
    expected = 3
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_large_array():
    """Test with a larger array"""
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    k = 3
    # Subarrays of length 3: [1,1,1], [1,1,1], ...
    # There are 8 such subarrays
    expected = 8
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_no_subarrays_sum_to_k():
    """Test when no subarrays sum to k"""
    nums = [1, 2, 3, 4]
    k = 10
    expected = 1
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_multiple_ways_to_sum():
    """Test with multiple different subarrays summing to k"""
    nums = [1, 2, 1, 2, 1]
    k = 3
    # Subarrays that sum to 3: [1,2], [2,1], [1,2], [2,1]
    expected = 4
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"


def test_k_zero():
    """Test when k is zero"""
    nums = [1, -1, 2, -2, 3]
    k = 0
    # Subarrays that sum to 0: [1,-1], [2,-2], [1,-1,2,-2]
    expected = 3
    result = k_sum_subarrays(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"
