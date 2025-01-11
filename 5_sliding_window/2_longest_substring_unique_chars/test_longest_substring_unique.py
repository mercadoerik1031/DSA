from longest_substring_unique import longest_unique_substring


def test_basic_case_abcba():
    assert longest_unique_substring("abcba") == 3  # "abc" or "cba"


def test_basic_case_bbbbb():
    assert longest_unique_substring("bbbbb") == 1  # "b"


def test_basic_case_pwwkew():
    assert longest_unique_substring("pwwkew") == 3  # "wke"


def test_edge_case_empty_string():
    assert longest_unique_substring("") == 0  # Empty string


def test_edge_case_single_character():
    assert longest_unique_substring("a") == 1  # Single character


def test_edge_case_all_same_characters():
    assert longest_unique_substring("aaaaa") == 1  # All characters are the same


def test_all_unique_characters():
    assert longest_unique_substring("abcdef") == 6  # All characters unique


def test_mixed_case_abacabc():
    assert longest_unique_substring("abacabc") == 3  # "abc"


def test_mixed_case_abcabcbb():
    assert longest_unique_substring("abcabcbb") == 3  # "abc"


def test_mixed_case_dvdf():
    assert longest_unique_substring("dvdf") == 3  # "vdf"


def test_special_characters_and_spaces():
    assert (
        longest_unique_substring("abc def ghi") == 7
    )  # "abc def" (space counts as unique)


def test_special_characters_with_symbols():
    assert longest_unique_substring("abc@123@def") == 7  # "123@def"


def test_case_sensitivity():
    assert longest_unique_substring("abcABC") == 6  # Case-sensitive unique string


def test_unicode_characters():
    assert longest_unique_substring("aäbcädef") == 6  # "bcädef" (Unicode support)


def test_empty_string():
    assert longest_unique_substring(" ") == 1
