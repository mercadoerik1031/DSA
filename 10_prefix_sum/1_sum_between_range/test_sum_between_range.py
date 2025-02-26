import pytest


from sum_between_range import sum_range


class TestSumRange:
    # Test cases with basic examples
    def test_basic_examples(self):
        arr = [3, -7, 6, 0, -2, 5]
        assert sum_range(arr, 0, 3) == 2  # 3 + (-7) + 6 + 0 = 2
        assert sum_range(arr, 2, 4) == 4  # 6 + 0 + (-2) = 4
        assert sum_range(arr, 2, 2) == 6  # Just the element at index 2, which is 6

    # Test with empty array
    def test_empty_array(self):
        with pytest.raises(IndexError):
            sum_range([], 0, 0)

    # Test with negative indexes
    def test_negative_indexes(self):
        arr = [3, -7, 6, 0, -2, 5]
        assert sum_range(arr, -1, -1) == 5  # Last element
        assert sum_range(arr, -3, -1) == 3  # (-2) + 5 = 3
        assert sum_range(arr, -6, -4) == 2  # 3 + (-7) + 6 = 2

    # Test with idx1 > idx2
    def test_reversed_indexes(self):
        arr = [3, -7, 6, 0, -2, 5]
        with pytest.raises(ValueError):
            sum_range(arr, 3, 0)

    # Test with out of bounds indexes
    def test_out_of_bounds(self):
        arr = [3, -7, 6, 0, -2, 5]
        with pytest.raises(IndexError):
            sum_range(arr, 0, 10)
        with pytest.raises(IndexError):
            sum_range(arr, -10, 2)

    # Test with array of all zeros
    def test_all_zeros(self):
        arr = [0, 0, 0, 0, 0]
        assert sum_range(arr, 1, 3) == 0
        assert sum_range(arr, 0, 4) == 0

    # Test with array of all same values
    def test_all_same_values(self):
        arr = [5, 5, 5, 5, 5]
        assert sum_range(arr, 1, 3) == 15  # 5 + 5 + 5 = 15
        assert sum_range(arr, 0, 4) == 25  # 5 * 5 = 25

    # Test with extreme values
    def test_extreme_values(self):
        arr = [10**9, -(10**9), 10**9]
        assert sum_range(arr, 0, 2) == 10**9  # 10^9 + (-10^9) + 10^9 = 10^9

    # Test the list of ranges functionality
    def test_list_of_ranges(self):
        arr = [3, -7, 6, 0, -2, 5]
        ranges = [(0, 3), (2, 4), (2, 2)]
        expected = [2, 4, 6]
        results = [sum_range(arr, start, end) for start, end in ranges]
        assert results == expected
