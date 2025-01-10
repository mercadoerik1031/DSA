import pytest
from happy_number import is_happy_number  # Assuming your function is in happy_number.py


def test_known_happy_numbers():
    """Test numbers that are known to be happy numbers"""
    happy_numbers = [
        1,
        7,
        10,
        13,
        19,
        23,
        28,
        31,
        32,
        44,
        49,
        68,
        70,
        79,
        82,
        86,
        91,
        94,
        97,
        100,
    ]
    for num in happy_numbers:
        assert is_happy_number(num) == True, f"{num} should be a happy number"


def test_known_unhappy_numbers():
    """Test numbers that are known to lead to cycles (unhappy numbers)"""
    unhappy_numbers = [2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 17, 18, 20]
    for num in unhappy_numbers:
        assert is_happy_number(num) == False, f"{num} should not be a happy number"


def test_edge_cases():
    """Test edge cases"""
    # Test single digit numbers
    assert is_happy_number(1) == True, "1 should be a happy number"
    assert is_happy_number(7) == True, "7 should be a happy number"
    assert is_happy_number(8) == False, "8 should not be a happy number"


def test_larger_numbers():
    """Test some larger numbers"""
    assert is_happy_number(989) == True, "989 should be a happy number"
    assert is_happy_number(999) == False, "999 should not be a happy number"
    assert is_happy_number(1000) == True, "1000 should be a happy number"


def test_specific_cycle_examples():
    """Test numbers that produce specific known cycles"""
    # 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
    cycle_numbers = [4, 16, 37, 58, 89, 145, 42, 20]
    for num in cycle_numbers:
        assert (
            is_happy_number(num) == False
        ), f"{num} should not be a happy number (part of cycle)"


def test_number_progression():
    """Test a number and verify its known progression"""
    # 19 -> 82 -> 68 -> 100 -> 1
    assert is_happy_number(19) == True, "19 should progress to 1"
    assert is_happy_number(82) == True, "82 should progress to 1"
    assert is_happy_number(68) == True, "68 should progress to 1"
    assert is_happy_number(100) == True, "100 should progress to 1"


def test_zero():
    """Test zero as input"""
    assert is_happy_number(0) == False, "0 should not be a happy number"


@pytest.mark.parametrize("input_num", [-1, -7, -19, -42, -100])
def test_negative_numbers(input_num):
    """Test negative numbers - these should raise ValueError"""
    with pytest.raises(ValueError):
        is_happy_number(input_num)
