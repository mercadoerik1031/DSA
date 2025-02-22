import pytest
from id_all_overlaps import id_all_overlaps


def test_basic_overlaps():
    intervals1 = [[1, 4], [5, 6], [9, 10]]
    intervals2 = [[2, 7], [8, 9]]
    assert id_all_overlaps(intervals1, intervals2) == [[2, 4], [5, 6], [9, 9]]


def test_no_overlaps():
    intervals1 = [[1, 2], [3, 4]]
    intervals2 = [[5, 6], [7, 8]]
    assert id_all_overlaps(intervals1, intervals2) == []


def test_complete_overlap():
    intervals1 = [[2, 5]]
    intervals2 = [[1, 6]]
    assert id_all_overlaps(intervals1, intervals2) == [[2, 5]]


def test_multiple_overlaps_with_one_interval():
    intervals1 = [[1, 10]]
    intervals2 = [[2, 3], [4, 5], [6, 7]]
    assert id_all_overlaps(intervals1, intervals2) == [[2, 3], [4, 5], [6, 7]]


def test_empty_arrays():
    intervals1 = []
    intervals2 = [[1, 2]]
    assert id_all_overlaps(intervals1, intervals2) == []
    assert id_all_overlaps(intervals2, intervals1) == []
    assert id_all_overlaps([], []) == []


def test_negative_numbers():
    intervals1 = [[-5, -3], [-2, 0]]
    intervals2 = [[-4, -1]]
    assert id_all_overlaps(intervals1, intervals2) == [[-4, -3], [-2, -1]]


def test_large_numbers():
    intervals1 = [[1000, 2000]]
    intervals2 = [[1500, 1800]]
    assert id_all_overlaps(intervals1, intervals2) == [[1500, 1800]]


def test_identical_intervals():
    intervals1 = [[1, 2], [3, 4]]
    intervals2 = [[1, 2], [3, 4]]
    assert id_all_overlaps(intervals1, intervals2) == [[1, 2], [3, 4]]


def test_nested_intervals():
    intervals1 = [[1, 10]]
    intervals2 = [[2, 3], [4, 5], [6, 7]]
    assert id_all_overlaps(intervals1, intervals2) == [[2, 3], [4, 5], [6, 7]]


# Error handling tests
def test_invalid_interval_format():
    with pytest.raises(IndexError):
        id_all_overlaps([[1]], [[1, 2]])

    with pytest.raises(TypeError):
        id_all_overlaps([[1, "2"]], [[1, 2]])


def test_invalid_input_type():
    with pytest.raises(TypeError):
        id_all_overlaps("not a list", [[1, 2]])

    with pytest.raises(TypeError):
        id_all_overlaps([[1, 2]], "not a list")
