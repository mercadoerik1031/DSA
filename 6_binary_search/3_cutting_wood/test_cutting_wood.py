from cutting_wood import find_height

def test_given_example() -> None:
    heights = [2, 6, 3, 8]
    k = 7
    assert find_height(k, heights) == 3

def test_single_tree() -> None:
    heights = [10]
    k = 5
    assert find_height(k, heights) == 5

def test_all_trees_same_height() -> None:
    heights = [5, 5, 5, 5]
    k = 10
    assert find_height(k, heights) == 2

def test_exact_wood_amount() -> None:
    heights = [4, 7, 2, 9]
    k = 6
    assert find_height(k, heights) == 5

def test_minimum_cut_possible() -> None:
    heights = [10, 15, 20]
    k = 15
    assert find_height(k, heights) == 10

def test_maximum_cut_scenario() -> None:
    heights = [1, 2, 3, 4, 5]
    k = 10
    assert find_height(k, heights) == 1

def test_large_height_difference() -> None:
    heights = [1, 100, 50, 75]
    k = 150
    assert find_height(k, heights) == 25