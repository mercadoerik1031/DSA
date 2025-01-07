from zero_stripping import zero_stripping
from typing import List


def test_basic_matrix():
    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    expected = [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
    zero_stripping(matrix)
    assert matrix == expected


def test_multiple_zeros():
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 0]]
    expected = [[1, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    zero_stripping(matrix)
    assert matrix == expected


def test_no_zeros():
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 2], [3, 4]]
    zero_stripping(matrix)
    assert matrix == expected


def test_all_zeros():
    matrix = [[0, 0], [0, 0]]
    expected = [[0, 0], [0, 0]]
    zero_stripping(matrix)
    assert matrix == expected


def test_single_element():
    matrix = [[1]]
    expected = [[1]]
    zero_stripping(matrix)
    assert matrix == expected


def test_single_zero():
    matrix = [[0]]
    expected = [[0]]
    zero_stripping(matrix)
    assert matrix == expected


def test_edge_cases():
    matrix = [[1, 0, 1], [1, 1, 1], [1, 0, 1]]
    expected = [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
    zero_stripping(matrix)
    assert matrix == expected
