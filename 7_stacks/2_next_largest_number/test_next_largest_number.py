from next_largest_number import largest_number_to_right


def test_given_example() -> None:
    nums = [5, 2, 4, 6, 1]
    assert largest_number_to_right(nums) == [6, 4, 6, -1, -1]
