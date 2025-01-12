from find_insertion_index import find_insertion_index


def test_target_exists_in_middle():
    """Test when target exists in the middle of the array"""
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 4
    assert find_insertion_index(nums, target) == 2


def test_target_exists_at_start():
    """Test when target exists at the start of the array"""
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 1
    assert find_insertion_index(nums, target) == 0


def test_target_exists_at_end():
    """Test when target exists at the end of the array"""
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 9
    assert find_insertion_index(nums, target) == 6


def test_target_should_be_inserted_in_middle():
    """Test when target should be inserted in the middle"""
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 6
    assert find_insertion_index(nums, target) == 4


def test_target_should_be_inserted_at_start():
    """Test when target should be inserted at the start"""
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 0
    assert find_insertion_index(nums, target) == 0


def test_empty_array():
    """Test with an empty array"""
    nums = []
    target = 1
    assert find_insertion_index(nums, target) == 0


def test_single_element_target_smaller():
    """Test single element array where target is smaller"""
    nums = [1]
    target = 0
    assert find_insertion_index(nums, target) == 0


def test_single_element_target_equal():
    """Test single element array where target equals the element"""
    nums = [1]
    target = 1
    assert find_insertion_index(nums, target) == 0


def test_two_elements_insert_between():
    """Test two element array where target should be inserted between"""
    nums = [1, 3]
    target = 2
    assert find_insertion_index(nums, target) == 1


def test_large_gap_between_elements():
    """Test array with large gaps between elements"""
    nums = [1, 10, 20, 30]
    target = 15
    assert find_insertion_index(nums, target) == 2


def test_very_large_gap():
    """Test array with a very large gap"""
    nums = [1, 1000000]
    target = 500000
    assert find_insertion_index(nums, target) == 1


def test_negative_numbers_insert():
    """Test array with negative numbers where target should be inserted"""
    nums = [-5, -3, -1, 0, 2]
    target = -4
    assert find_insertion_index(nums, target) == 1


def test_negative_numbers_exists():
    """Test array with negative numbers where target exists"""
    nums = [-5, -3, -1, 0, 2]
    target = -5
    assert find_insertion_index(nums, target) == 0


def test_all_negative_numbers():
    """Test array with all negative numbers"""
    nums = [-5, -4, -3, -2, -1]
    target = -6
    assert find_insertion_index(nums, target) == 0


def test_target_between_consecutive_numbers():
    """Test when target should be inserted between consecutive numbers"""
    nums = [1, 2, 3, 4, 5]
    target = 3.5
    assert find_insertion_index(nums, target) == 3
