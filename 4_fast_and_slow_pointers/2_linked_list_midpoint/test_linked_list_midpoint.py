from linked_list_midpoint import find_middle_node, ListNode
from typing import Optional, List


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    head = None
    for value in reversed(values):
        node = ListNode(value)
        node.next = head
        head = node
    return head


# ---------------------- TESTS ----------------------------


def test_empty_list() -> None:
    """Test case for empty linked list"""
    assert find_middle_node(None) is None


def test_single_node() -> None:
    """Test case for linked list with single node"""
    head = create_linked_list([1])
    result = find_middle_node(head)
    assert result.val == 1


def test_two_nodes() -> None:
    """Test case for linked list with two nodes"""
    head = create_linked_list([1, 2])
    result = find_middle_node(head)
    assert result.val == 2


def test_odd_length_list() -> None:
    """Test case for linked list with odd number of nodes"""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = find_middle_node(head)
    assert result.val == 3


def test_even_length_list() -> None:
    """Test case for linked list with even number of nodes"""
    head = create_linked_list([1, 2, 3, 4])
    result = find_middle_node(head)
    assert result.val == 3


def test_example_one() -> None:
    """Test case for the first example in problem description"""
    head = create_linked_list([1, 2, 4, 7, 3])
    result = find_middle_node(head)
    assert result.val == 4


def test_example_two() -> None:
    """Test case for the second example in problem description"""
    head = create_linked_list([1, 2, 4, 7])
    result = find_middle_node(head)
    assert result.val == 4


def test_large_list() -> None:
    """Test case for a larger linked list"""
    values = list(range(1, 11))  # [1, 2, ..., 10]
    head = create_linked_list(values)
    result = find_middle_node(head)
    assert result.val == 6


def test_duplicate_values() -> None:
    """Test case for linked list with duplicate values"""
    head = create_linked_list([1, 2, 2, 2, 1])
    result = find_middle_node(head)
    assert result.val == 2
