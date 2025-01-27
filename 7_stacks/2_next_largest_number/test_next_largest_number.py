from next_largest_number import largest_number_to_right


def test_given_example() -> None:
    nums = [5, 2, 4, 6, 1]
    assert largest_number_to_right(nums) == [6, 4, 6, -1, -1]


def test_empty_list() -> None:
    nums = []
    assert largest_number_to_right(nums) == []


def test_single_element() -> None:
    nums = [10]
    assert largest_number_to_right(nums) == [-1]


def test_all_elements_same() -> None:
    nums = [7, 7, 7, 7]
    assert largest_number_to_right(nums) == [-1, -1, -1, -1]


def test_no_larger_element() -> None:
    nums = [9, 8, 7, 6]
    assert largest_number_to_right(nums) == [-1, -1, -1, -1]


def test_decreasing_order() -> None:
    nums = [10, 9, 8, 7, 6]
    assert largest_number_to_right(nums) == [-1, -1, -1, -1, -1]


def test_increasing_order() -> None:
    nums = [1, 2, 3, 4, 5]
    assert largest_number_to_right(nums) == [2, 3, 4, 5, -1]


def test_mixed_values() -> None:
    nums = [4, 5, 2, 10, 1, 3]
    assert largest_number_to_right(nums) == [5, 10, 10, -1, 3, -1]


def test_large_numbers() -> None:
    nums = [1000000000, 999999999, 1000000001, 999999998]
    assert largest_number_to_right(nums) == [1000000001, 1000000001, -1, -1]
