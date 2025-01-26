from rotated_sorted_arr import rotated_binary_search
import pytest
from typing import List


def test_given_example() -> None:
    nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target = 1
    assert rotated_binary_search(nums, target) == 2


def test_given_example() -> None:
    """Test the example from the problem statement"""
    nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target = 1
    assert rotated_binary_search(nums, target) == 2


def test_target_at_start() -> None:
    """Test when target is at the start of the array"""
    nums = [5, 6, 7, 1, 2, 3, 4]
    target = 5
    assert rotated_binary_search(nums, target) == 0


def test_target_at_end() -> None:
    """Test when target is at the end of the array"""
    nums = [5, 6, 7, 1, 2, 3, 4]
    target = 4
    assert rotated_binary_search(nums, target) == 6


def test_no_rotation() -> None:
    """Test with a sorted array with no rotation"""
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 4
    assert rotated_binary_search(nums, target) == 3


def test_full_rotation() -> None:
    """Test with array rotated back to original position"""
    nums = [1, 2, 3, 4, 5]
    target = 3
    assert rotated_binary_search(nums, target) == 2


def test_target_not_found() -> None:
    """Test when target is not in the array"""
    nums = [4, 5, 6, 7, 1, 2, 3]
    target = 8
    assert rotated_binary_search(nums, target) == -1


def test_single_element() -> None:
    """Test with array containing only one element"""
    nums = [1]
    assert rotated_binary_search(nums, 1) == 0
    assert rotated_binary_search(nums, 2) == -1


def test_two_elements() -> None:
    """Test with array containing two elements"""
    nums = [2, 1]
    assert rotated_binary_search(nums, 1) == 1
    assert rotated_binary_search(nums, 2) == 0
    assert rotated_binary_search(nums, 3) == -1


def test_empty_array() -> None:
    """Test with an empty array"""
    nums: List[int] = []
    assert rotated_binary_search(nums, 5) == -1


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([3, 4, 5, 1, 2], 4, 1),  # Target in first half
        ([3, 4, 5, 1, 2], 1, 3),  # Target in second half
        ([3, 4, 5, 1, 2], 2, 4),  # Target at end
        ([3, 4, 5, 1, 2], 3, 0),  # Target at start
        ([3, 4, 5, 1, 2], 6, -1),  # Target not present
    ],
)
def test_various_rotations(nums: List[int], target: int, expected: int) -> None:
    """Test different rotation patterns with targets in different positions"""
    assert rotated_binary_search(nums, target) == expected


def test_pivot_at_middle() -> None:
    """Test when the rotation pivot is at the middle of the array"""
    nums = [6, 7, 8, 1, 2, 3, 4, 5]
    assert rotated_binary_search(nums, 8) == 2
    assert rotated_binary_search(nums, 1) == 3


def test_duplicate_values() -> None:
    """Test behavior with duplicate values (if allowed by problem constraints)"""
    nums = [3, 3, 3, 1, 2, 3]
    target = 1
    result = rotated_binary_search(nums, target)
    assert result == 3


def test_large_numbers() -> None:
    """Test with large numbers in the array"""
    nums = [1000000, 1000001, 1000002, 1, 2, 3]
    assert rotated_binary_search(nums, 1000001) == 1
    assert rotated_binary_search(nums, 2) == 4
