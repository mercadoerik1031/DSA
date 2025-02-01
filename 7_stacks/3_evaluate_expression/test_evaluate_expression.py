import pytest
from evaluate_expression import evaluate_expression


# Parameterized test cases
@pytest.mark.parametrize(
    "expression,expected",
    [
        ("18-(7+(2-4))", 13),  # Provided example
        ("1+1", 2),  # Simple addition
        ("2-3+4", 3),  # Mixed addition and subtraction
        ("10+(2-3)", 9),  # Parentheses with subtraction
        ("10-(2-3)", 11),  # Parentheses with negative sign inversion
        ("5", 5),  # Single number
        ("((1+2)-3)", 0),  # Nested parentheses that cancel out
        (
            "10- ( 2 + (3 - (4 + (5 - 6))))",
            10 - (2 + (3 - (4 + (5 - 6)))),
        ),  # More complex nesting with spaces
        ("0", 0),  # Zero
        ("123", 123),  # Multi-digit number without any operator
    ],
)


def test_evaluate_expression(expression, expected):
    assert evaluate_expression(expression) == expected


# Additional tests for edge cases
def test_expression_with_spaces():
    expression = " 12 + ( 4 -  2 ) "
    expected = 12 + (4 - 2)
    assert evaluate_expression(expression) == expected


def test_expression_without_parentheses():
    expression = "7-2+10-3"
    expected = 7 - 2 + 10 - 3
    assert evaluate_expression(expression) == expected


def test_expression_complex():
    # This expression tests multiple digit numbers and nested parentheses.
    expression = "100-(50+(25-5)+(10-(2+3)))"
    # Expected evaluation:
    # = 100 - (50 + (25-5) + (10 - (2+3)))
    # = 100 - (50 + 20 + (10 - 5))
    # = 100 - (50 + 20 + 5)
    # = 100 - 75 = 25
    expected = 25
    assert evaluate_expression(expression) == expected
