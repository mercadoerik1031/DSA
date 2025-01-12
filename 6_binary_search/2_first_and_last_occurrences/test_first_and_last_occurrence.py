from first_and_last_occurrences import first_and_last_occurrence


def test_example_case():
    """Test the example provided in the problem statement"""
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 4
    assert first_and_last_occurrence(nums, target) == [3, 5]


def test_target_not_found():
    """Test when target is not present in the array"""
    nums = [1, 2, 3, 5, 6, 7]
    target = 4
    assert first_and_last_occurrence(nums, target) == [-1, -1]


def test_single_occurrence():
    """Test when target appears only once"""
    nums = [1, 2, 3, 4, 5]
    target = 4
    assert first_and_last_occurrence(nums, target) == [3, 3]


def test_all_same_numbers():
    """Test when array contains all same numbers"""
    nums = [5, 5, 5, 5, 5]
    target = 5
    assert first_and_last_occurrence(nums, target) == [0, 4]


def test_target_at_boundaries():
    """Test when target is at array boundaries"""
    nums = [4, 4, 4, 5, 6, 7, 8]
    target = 4
    assert first_and_last_occurrence(nums, target) == [0, 2]

    nums = [1, 2, 3, 4, 4, 4]
    target = 4
    assert first_and_last_occurrence(nums, target) == [3, 5]


def test_empty_array():
    """Test with empty array"""
    nums = []
    target = 5
    assert first_and_last_occurrence(nums, target) == [-1, -1]


def test_single_element():
    """Test array with single element"""
    nums = [5]
    target = 5
    assert first_and_last_occurrence(nums, target) == [0, 0]

    nums = [3]
    target = 5
    assert first_and_last_occurrence(nums, target) == [-1, -1]


def test_two_elements():
    """Test array with two elements"""
    nums = [5, 5]
    target = 5
    assert first_and_last_occurrence(nums, target) == [0, 1]

    nums = [4, 5]
    target = 5
    assert first_and_last_occurrence(nums, target) == [1, 1]


def test_target_out_of_bounds():
    """Test when target is outside array range"""
    nums = [2, 3, 4, 5, 6]
    target = 1  # Less than smallest
    assert first_and_last_occurrence(nums, target) == [-1, -1]

    target = 7  # Greater than largest
    assert first_and_last_occurrence(nums, target) == [-1, -1]


def test_large_range():
    """Test with array containing large numbers"""
    nums = [10, 10, 10, 20, 20, 20, 20, 30, 30]
    target = 20
    assert first_and_last_occurrence(nums, target) == [3, 6]


def test_negative_numbers():
    """Test with negative numbers"""
    nums = [-5, -5, -5, -3, -2, -1]
    target = -5
    assert first_and_last_occurrence(nums, target) == [0, 2]


def test_repeated_non_target():
    """Test with repeated numbers that aren't the target"""
    nums = [1, 1, 1, 2, 2, 3, 3, 3]
    target = 2
    assert first_and_last_occurrence(nums, target) == [3, 4]
