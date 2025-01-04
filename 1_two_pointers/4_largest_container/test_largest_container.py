from largest_container import largest_container


def test_empty_array() -> None:
    heights = []
    result = largest_container(heights)
    assert result == 0


def test_array_one_element() -> None:
    heights = [1]
    result = largest_container(heights)
    assert result == 0


def test_container_no_water() -> None:
    heights = [0, 1, 0]
    result = largest_container(heights)
    assert result == 0


def test_all_heights_equal() -> None:
    heights = [3, 3, 3, 3]
    result = largest_container(heights)
    assert result == 9


def test_increasing_heights() -> None:
    heights = [1, 2, 3]
    result = largest_container(heights)
    assert result == 2


def test_decreasing_heights() -> None:
    heights = [3, 2, 1]
    result = largest_container(heights)
    assert result == 2


def test_valley_shape() -> None:
    heights = [5, 2, 1, 2, 5]
    result = largest_container(heights)
    assert result == 20


def test_mountain_shape() -> None:
    heights = [1, 3, 5, 3, 1]
    result = largest_container(heights)
    assert result == 6


def test_alternating_heights() -> None:
    heights = [1, 3, 1, 3, 1, 3]
    result = largest_container(heights)
    assert result == 12


def test_large_numbers() -> None:
    heights = [10000, 1, 1, 1, 10000]
    result = largest_container(heights)
    assert result == 40000


def test_negative_numbers() -> None:
    heights = [-1, -2, -3, -4]
    result = largest_container(heights)
    assert result == 0


def test_sparse_array() -> None:
    heights = [1, 0, 0, 0, 1]
    result = largest_container(heights)
    assert result == 4


def test_uneven_peaks() -> None:
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = largest_container(heights)
    assert result == 49


def test_repeated_elements() -> None:
    heights = [1, 2, 2, 2, 1]
    result = largest_container(heights)
    assert result == 4


def test_single_high_peak() -> None:
    heights = [1, 1, 10, 1, 1]
    result = largest_container(heights)
    assert result == 4
