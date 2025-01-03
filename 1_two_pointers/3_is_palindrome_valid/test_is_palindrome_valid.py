from is_palindrome_valid import is_valid_palindrome


def test_empty_string() -> None:
    s = ""
    result = is_valid_palindrome(s)
    assert result == True


def test_single_char() -> None:
    s = "a"
    result = is_valid_palindrome(s)
    assert result == True


def test_two_chars() -> None:
    s = "aa"
    result = is_valid_palindrome(s)
    assert result == True


def test_non_palindrome_two_chars() -> None:
    s = "ab"
    result = is_valid_palindrome(s)
    assert result == False


def test_str_no_alphanumeric() -> None:
    s = "!, (?)"
    result = is_valid_palindrome(s)
    assert result == True


def test_palindrome_punctuation_and_numbers() -> None:
    s = "12.02.2021"
    result = is_valid_palindrome(s)
    assert result == True


def test_non_palindrome_punctuation_and_numbers() -> None:
    s = "21.02.2021"
    result = is_valid_palindrome(s)
    assert result == False


def test_non_palindrome_with_punctuation() -> None:
    s = "hello, world!"
    result = is_valid_palindrome(s)
    assert result == False


def test_lowercase_only_palindrome() -> None:
    s = "racecar"
    result = is_valid_palindrome(s)
    assert result == True


def test_numbers_only_palindrome() -> None:
    s = "12321"
    result = is_valid_palindrome(s)
    assert result == True


def test_mixed_alphanumeric_palindrome() -> None:
    s = "a1b2b1a"
    result = is_valid_palindrome(s)
    assert result == True


def test_with_spaces_palindrome() -> None:
    s = "never odd or even"
    result = is_valid_palindrome(s)
    assert result == True


def test_with_punctuation_palindrome() -> None:
    s = "a man, a plan, a canal: panama"
    result = is_valid_palindrome(s)
    assert result == True


def test_multiple_spaces() -> None:
    s = "  race   a car  "
    result = is_valid_palindrome(s)
    assert result == False


def test_only_punctuation() -> None:
    s = ".,?!"
    result = is_valid_palindrome(s)
    assert result == True


def test_only_spaces() -> None:
    s = "     "
    result = is_valid_palindrome(s)
    assert result == True


def test_mixed_content_non_palindrome() -> None:
    s = "ab1, 2ba"
    result = is_valid_palindrome(s)
    assert result == False


def test_complex_mixed_palindrome() -> None:
    s = "1a2, 2a1"
    result = is_valid_palindrome(s)
    assert result == True


def test_sentence_with_punctuation_non_palindrome() -> None:
    s = "hello, how are you?"
    result = is_valid_palindrome(s)
    assert result == False


def test_palindrome_with_all_allowed_chars() -> None:
    s = "ab12 21ba"
    result = is_valid_palindrome(s)
    assert result == True
