import pytest
from pair_sum import pair_sum

def test_pair_sum_empty_array() -> None:
    nums = []
    target = 0
    result = pair_sum(nums, target)
    assert result == []

def test_pair_sum_one_element() -> None:
    nums = [1]
    target = 1
    result = pair_sum(nums, target)
    assert result == []

def test_pair_sum_two_element_contains_pair() -> None:
    nums = [2, 3]
    target = 5
    result = pair_sum(nums, target)
    assert result == [0, 1]

def test_pair_sum_two_element_no_pair() -> None:
    nums = [2, 4]
    target = 5
    result = pair_sum(nums, target)
    assert result == []

def test_pair_sum_duplicate_values() -> None:
    nums = [2, 2, 3]
    target = 5
    result = pair_sum(nums, target)
    assert result == [0, 2] or result == [1, 2]

def test_pair_sum_with_negative() -> None:
    nums = [-1, 2, 3]
    target = 2
    result = pair_sum(nums, target)
    assert result == [0, 2]

def test_pair_sum_both_numbers_of_target_negative() -> None:
    nums = [-3, -2, -1]
    target = -5
    result = pair_sum(nums, target)
    assert result == [0, 1]

def test_pair_sum_multiple_pairs() -> None:
    nums = [1, 2, 3, 4, 5, 6]
    target = 7
    result = pair_sum(nums, target)
    assert result == [1, 4] or result == [0, 5]

def test_pair_sum_large_array() -> None:
    nums = list(range(1, 10**6))
    target = 1999997
    result = pair_sum(nums, target)
    assert result == [999997, 999998]

def test_pair_sum_only_negative_numbers() -> None:
    nums = [-5, -4, -3, -2, -1]
    target = -6
    result = pair_sum(nums, target)
    assert result == [0, 4]

def test_pair_sum_positive_array_negative_target() -> None:
    nums = [1, 2, 3, 4, 5]
    target = -1
    result = pair_sum(nums, target)
    assert result == []

def test_pair_sum_equal_values() -> None:
    nums = [3, 3]
    target = 6
    result = pair_sum(nums, target)
    assert result == [0, 1]

def test_pair_sum_target_zero() -> None:
    nums = [-3, -2, 0, 2, 3]
    target = 0
    result = pair_sum(nums, target)
    assert result == [0, 4] or result == [1, 3]

def test_pair_sum_large_target() -> None:
    nums = [1, 2, 3, 4, 5]
    target = 100
    result = pair_sum(nums, target)
    assert result == []