import pytest
from valid_parenthesis import is_valid_parenthesis


def test_given_example_one() -> None:
    """Test the first example from the problem statement"""
    s = "([]{})"
    assert is_valid_parenthesis(s) == True


def test_given_example_two() -> None:
    """Test the second example from the problem statement"""
    s = "([]{)}"
    assert is_valid_parenthesis(s) == False


def test_empty_string() -> None:
    """An empty string should be considered valid"""
    s = ""
    assert is_valid_parenthesis(s) == True


def test_single_pair() -> None:
    """Test simple cases with single pairs"""
    assert is_valid_parenthesis("()") == True
    assert is_valid_parenthesis("[]") == True
    assert is_valid_parenthesis("{}") == True


def test_nested_pairs() -> None:
    """Test deeply nested parentheses"""
    assert is_valid_parenthesis("((()))") == True
    assert is_valid_parenthesis("[{([])}]") == True
    assert is_valid_parenthesis("{[()]}") == True


def test_invalid_closure_order() -> None:
    """Test cases where closing order is wrong"""
    assert is_valid_parenthesis("([)]") == False
    assert is_valid_parenthesis("{[}]") == False
    assert is_valid_parenthesis("[(])") == False


def test_unmatched_opening() -> None:
    """Test cases with unmatched opening brackets"""
    assert is_valid_parenthesis("((") == False
    assert is_valid_parenthesis("[{(") == False
    assert is_valid_parenthesis("({[") == False


def test_unmatched_closing() -> None:
    """Test cases with unmatched closing brackets"""
    assert is_valid_parenthesis("))") == False
    assert is_valid_parenthesis("}]]") == False
    assert is_valid_parenthesis("])}") == False


def test_mixed_invalid() -> None:
    """Test cases mixing valid and invalid patterns"""
    assert is_valid_parenthesis("()][") == False
    assert is_valid_parenthesis("([)]{}") == False
    assert is_valid_parenthesis("{[]})(") == False


def test_single_brackets() -> None:
    """Test single brackets which are always invalid"""
    assert is_valid_parenthesis("(") == False
    assert is_valid_parenthesis("]") == False
    assert is_valid_parenthesis("{") == False
    assert is_valid_parenthesis("}") == False


@pytest.mark.parametrize(
    "input_str", ["([]{}){()}[[()]]", "{{}}[[]]()(){}[]", "{[()]}([]){{}}"]
)
def test_complex_valid_cases(input_str: str) -> None:
    """Test various complex but valid combinations"""
    assert is_valid_parenthesis(input_str) == True


@pytest.mark.parametrize(
    "input_str", ["(", ")", "(]", "([)]", "((())", "()))", "{[]}}"]
)
def test_various_invalid_cases(input_str: str) -> None:
    """Test various invalid combinations"""
    assert is_valid_parenthesis(input_str) == False
