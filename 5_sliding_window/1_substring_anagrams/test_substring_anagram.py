from substring_anagram import count_substring_anagram


def test_basic_case():
    assert count_substring_anagram("caabab", "aba") == 3


def test_no_anagrams():
    assert count_substring_anagram("abcdefg", "hij") == 0


def test_entire_string_is_anagram():
    assert count_substring_anagram("abc", "abc") == 1


def test_empty_s():
    assert count_substring_anagram("", "abc") == 0


def test_empty_t():
    assert count_substring_anagram("abc", "") == 0


def test_empty_s_and_t():
    assert count_substring_anagram("", "") == 0


def test_t_larger_than_s():
    assert count_substring_anagram("abc", "abcd") == 0


def test_repeated_characters():
    assert count_substring_anagram("aaaaaa", "aa") == 5


def test_overlapping_anagrams():
    assert count_substring_anagram("abababab", "ab") == 7


def test_non_overlapping_anagrams():
    assert count_substring_anagram("abxabay", "ab") == 2


def test_single_character_match():
    assert count_substring_anagram("aaaaa", "a") == 5


def test_single_character_no_match():
    assert count_substring_anagram("aaaaa", "b") == 0
