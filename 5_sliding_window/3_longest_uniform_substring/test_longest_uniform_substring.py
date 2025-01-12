from longest_uniform_substring import longest_uniform_substring


def test_basic_case():
    """Test the example case provided in the problem statement"""
    assert longest_uniform_substring("aabcdcca", 2) == 5


def test_empty_string():
    """Test with empty string"""
    assert longest_uniform_substring("", 2) == 0


def test_single_character():
    """Test with a single character string"""
    assert longest_uniform_substring("a", 1) == 1


def test_already_uniform():
    """Test with already uniform string"""
    assert longest_uniform_substring("aaaa", 2) == 4


def test_no_replacements_allowed():
    """Test when k = 0"""
    assert longest_uniform_substring("abcde", 0) == 1
    assert longest_uniform_substring("aabaa", 0) == 2


def test_all_replacements_allowed():
    """Test when k equals string length"""
    s = "abcde"
    assert longest_uniform_substring(s, len(s)) == len(s)


def test_partial_replacements():
    """Test various scenarios with partial replacements"""
    test_cases = [
        ("aabab", 1, 4),  # Can make "aaaa" by replacing one 'b'
        ("abcba", 2, 4),  # Can make "bbbb" by replacing 'a' and 'c'
        ("aabaab", 2, 6),  # Can make "aaaaaa" by replacing two 'b's
        ("abcdef", 3, 4),  # Can make any character appear 4 times
    ]

    for s, k, expected in test_cases:
        assert longest_uniform_substring(s, k) == expected


def test_multiple_possible_solutions():
    """Test cases where multiple solutions are possible"""
    # "xxxxx" or "aaaaa" are both valid 5-length solutions
    assert longest_uniform_substring("axxaxa", 2) == 5


def test_edge_cases():
    """Test edge cases with special patterns"""
    test_cases = [
        ("a" * 1000, 5, 1000),  # Very long string of same character
        ("ab" * 500, 499, 999),  # Alternating pattern
        ("abc" * 333, 500, 751),  # Repeating pattern
    ]

    for s, k, expected in test_cases:
        assert longest_uniform_substring(s, k) == expected


def test_k_greater_than_needed():
    """Test when k is larger than necessary"""
    assert longest_uniform_substring("abc", 10) == 3


def test_different_characters():
    """Test with strings containing various ASCII characters"""
    assert longest_uniform_substring("123!@#", 2) == 3
    assert longest_uniform_substring("aA1!", 2) == 3


def test_invalid_inputs():
    """Test handling of invalid k values"""
    import pytest

    with pytest.raises(ValueError):
        longest_uniform_substring("abc", -1)
