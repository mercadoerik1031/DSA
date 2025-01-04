from pair_sum_unsorted import pair_sum_unsorted


def test_basic_positive_numbers():
    assert sorted(pair_sum_unsorted([1, 2, 3, 4], 7)) == [2, 3]


def test_with_negative_numbers():
    assert sorted(pair_sum_unsorted([-1, 3, 4, 2], 2)) == [0, 1]


def test_multiple_valid_pairs():
    # If multiple pairs exist, any valid pair is acceptable
    result = pair_sum_unsorted([1, 5, 2, 4, 3], 6)
    assert sorted(result) == [0, 1] or result == [2, 3]


def test_no_solution():
    assert pair_sum_unsorted([1, 2, 3, 4], 10) == []


def test_same_numbers():
    assert sorted(pair_sum_unsorted([2, 2, 4], 4)) == [0, 1]


def test_zero_sum():
    assert sorted(pair_sum_unsorted([-2, 0, 2, 4], 0)) == [0, 2]


def test_all_negative_numbers():
    assert sorted(pair_sum_unsorted([-4, -2, -1, -3], -5)) == [0, 2]


def test_single_number():
    assert pair_sum_unsorted([5], 5) == []


def test_empty_array():
    assert pair_sum_unsorted([], 5) == []


def test_minimal_array():
    assert sorted(pair_sum_unsorted([1, 2], 3)) == [0, 1]


def test_large_numbers():
    assert sorted(pair_sum_unsorted([1000000, 2000000], 3000000)) == [0, 1]


def test_same_index_not_used():
    assert pair_sum_unsorted([4], 8) == []
