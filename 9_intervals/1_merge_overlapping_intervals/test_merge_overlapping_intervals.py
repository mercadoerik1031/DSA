import pytest
from merge_overlapping_intervals import merge_intervals


def test_basic_merge():
    intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
    assert merge_intervals(intervals) == [[1, 5], [6, 8]]


def test_no_overlap():
    intervals = [[1, 2], [4, 5], [7, 8]]
    assert merge_intervals(intervals) == [[1, 2], [4, 5], [7, 8]]


def test_complete_overlap():
    intervals = [[1, 4], [2, 3]]
    assert merge_intervals(intervals) == [[1, 4]]


def test_single_interval():
    intervals = [[1, 2]]
    assert merge_intervals(intervals) == [[1, 2]]


def test_adjacent_intervals():
    intervals = [[1, 2], [2, 3], [3, 4]]
    assert merge_intervals(intervals) == [[1, 4]]


def test_nested_intervals():
    intervals = [[1, 6], [2, 4], [3, 5]]
    assert merge_intervals(intervals) == [[1, 6]]


def test_unsorted_intervals():
    intervals = [[3, 6], [1, 2], [8, 10], [2, 4]]
    assert merge_intervals(intervals) == [[1, 6], [8, 10]]


def test_partial_overlap_chain():
    intervals = [[1, 3], [2, 4], [3, 5], [4, 6]]
    assert merge_intervals(intervals) == [[1, 6]]


def test_same_start_different_end():
    intervals = [[1, 4], [1, 5], [1, 3]]
    assert merge_intervals(intervals) == [[1, 5]]


def test_different_start_same_end():
    intervals = [[1, 5], [2, 5], [3, 5]]
    assert merge_intervals(intervals) == [[1, 5]]


def test_large_numbers():
    intervals = [[1000000, 2000000], [1500000, 2500000]]
    assert merge_intervals(intervals) == [[1000000, 2500000]]


def test_negative_numbers():
    intervals = [[-4, -2], [-3, -1], [0, 2]]
    assert merge_intervals(intervals) == [[-4, -1], [0, 2]]


# Edge cases and error handling
def test_empty_list():
    with pytest.raises(IndexError):
        merge_intervals([])


def test_invalid_interval():
    with pytest.raises(TypeError):
        merge_intervals([[1, "2"], [3, 4]])
