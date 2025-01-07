from typing import List, Optional
from reverse_single_linked_list import ListNode, reverse_linked_list


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ------------------------------------ TESTS ---------------------------------------------


def get_node_addresses(head: Optional[ListNode]) -> List[int]:
    """Get memory addresses of all nodes in the list."""
    addresses = []
    current = head
    while current:
        addresses.append(id(current))
        current = current.next
    return addresses


def test_simple_linked_list():
    values = [1, 2, 3, 4]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_empty_list():
    result = reverse_linked_list(None)
    assert result is None


def test_single_node():
    values = [1]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values


def test_two_nodes():
    values = [1, 2]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


# Data Type Edge Cases
def test_negative_numbers():
    values = [-1, -2, -3, -4, -5]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_mixed_positive_negative():
    values = [-1, 0, 1, -2, 2]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_large_numbers():
    values = [1000000, -1000000, 999999, -999999]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_zero_values():
    values = [0, 0, 0, 0]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_duplicate_values():
    values = [1, 1, 2, 2, 3, 3]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_alternating_values():
    values = [1, 2, 1, 2, 1, 2]
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_large_list():
    values = list(range(10000))
    head = create_linked_list(values)
    result = reverse_linked_list(head)
    assert linked_list_to_list(result) == values[::-1]


def test_node_reuse():
    """Test that the function reuses the original nodes rather than creating new ones."""
    values = [1, 2, 3, 4]
    head = create_linked_list(values)
    original_addresses = get_node_addresses(head)
    result = reverse_linked_list(head)
    new_addresses = get_node_addresses(result)
    assert sorted(original_addresses) == sorted(new_addresses)
