from rotated_sorted_arr import rotated_binary_search

def test_given_example() -> None:
    nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target = 1
    assert rotated_binary_search(nums, target) == 2