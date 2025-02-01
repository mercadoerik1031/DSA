from k_most_frequent_strings import Pair, k_most_frequent_strs


def test_basic_case():
    strs = ["go", "coding", "byte", "byte", "go", "interview", "go"]
    k = 2
    expected = ["go", "byte"]
    assert k_most_frequent_strs(strs, k) == expected


def test_single_string():
    strs = ["hello", "hello", "hello"]
    k = 1
    expected = ["hello"]
    assert k_most_frequent_strs(strs, k) == expected


def test_equal_frequencies_lexicographic_order():
    strs = ["apple", "banana", "apple", "banana", "carrot"]
    k = 2
    expected = [
        "apple",
        "banana",
    ]
    assert k_most_frequent_strs(strs, k) == expected


def test_all_unique_strings():
    strs = ["zebra", "apple", "banana", "cat"]
    k = 2
    expected = [
        "apple",
        "banana",
    ]
    assert sorted(k_most_frequent_strs(strs, k)) == sorted(expected)


def test_large_k_value():
    strs = ["a", "b", "c", "a", "b", "c", "d"]
    k = 3
    expected = ["a", "b", "c"]
    assert k_most_frequent_strs(strs, k) == expected


def test_edge_case_empty_list():
    strs = []
    k = 0
    expected = []
    assert k_most_frequent_strs(strs, k) == expected


def test_edge_case_k_equals_1():
    strs = ["apple", "apple", "banana"]
    k = 1
    expected = ["apple"]
    assert k_most_frequent_strs(strs, k) == expected
