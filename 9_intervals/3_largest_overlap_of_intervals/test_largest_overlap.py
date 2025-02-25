from largest_overlap import largest_overlap


def test_example_case():
    intervals = [[1, 3], [2, 6], [4, 8], [6, 7], [5, 7]]
    assert largest_overlap(intervals) == 3


def test_no_overlap():
    intervals = [[1, 2], [3, 4], [5, 6]]
    assert largest_overlap(intervals) == 1


def test_complete_overlap():
    intervals = [[1, 10], [2, 5], [3, 4]]
    assert largest_overlap(intervals) == 3


def test_single_interval():
    intervals = [[1, 5]]
    assert largest_overlap(intervals) == 1


def test_same_start_point():
    intervals = [[1, 5], [1, 3], [1, 10]]
    assert largest_overlap(intervals) == 3


def test_same_end_point():
    intervals = [[1, 5], [2, 5], [3, 5]]
    assert largest_overlap(intervals) == 3


def test_start_equals_end():
    # Testing when one interval's end equals another's start
    intervals = [[1, 3], [3, 5], [5, 7]]
    assert largest_overlap(intervals) == 1


def test_large_numbers():
    intervals = [[1000000, 2000000], [1500000, 2500000], [1800000, 2200000]]
    assert largest_overlap(intervals) == 3


def test_unsorted_intervals():
    intervals = [[5, 7], [1, 3], [6, 7], [2, 6], [4, 8]]
    assert largest_overlap(intervals) == 3


def test_nested_intervals():
    intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]
    assert largest_overlap(intervals) == 5


def test_edge_case_sorting():
    # Test the edge case where we need to sort properly by both position and type
    intervals = [[1, 2], [2, 3]]
    assert largest_overlap(intervals) == 1
