from triplet_sum import triplet_sum


def test_triplet_sum_example() -> None:
    nums = [0, -1, 2, -3, 1]
    result = triplet_sum(nums)
    assert result == [[-3, 1, 2], [-1, 0, 1]]


def test_triplet_sum_empty_array() -> None:
    nums = []
    result = triplet_sum(nums)
    assert result == []


def test_triplet_sum_one_element() -> None:
    nums = [0]
    result = triplet_sum(nums)
    assert result == []


def test_triplet_sum_two_element() -> None:
    nums = [1, -1]
    result = triplet_sum(nums)
    assert result == []


def test_triplet_sum_same_values() -> None:
    nums = [0, 0, 0]
    result = triplet_sum(nums)
    assert result == [[0, 0, 0]]


def test_triplet_sum_no_triplet_sum() -> None:
    nums = [1, 0, 1]
    result = triplet_sum(nums)
    assert result == []


def test_triplet_sum_duplicate_triplets() -> None:
    nums = [0, 0, 1, -1, 1, -1]
    result = triplet_sum(nums)
    assert result == [[-1, 0, 1]]


def test_triplet_sum_all_negative() -> None:
    nums = [-1, -2, -3, -4, -5]
    result = triplet_sum(nums)
    assert result == []


def test_triplet_sum_all_positive() -> None:
    nums = [1, 2, 3, 4, 5]
    result = triplet_sum(nums)
    assert result == []


def test_triplet_sum_multiple_solutions() -> None:
    nums = [-2, -1, 0, 1, 2, 3, -3]
    result = triplet_sum(nums)
    assert result == [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]


def test_triplet_sum_large_numbers() -> None:
    nums = [-1000, 1000, 0, -2000, 2000]
    result = triplet_sum(nums)
    assert result == [[-2000, 0, 2000], [-1000, 0, 1000]]


def test_triplet_sum_multiple_duplicates() -> None:
    nums = [-1, -1, -1, 0, 0, 1, 2, 2]
    result = triplet_sum(nums)
    assert result == [[-1, -1, 2], [-1, 0, 1]]
