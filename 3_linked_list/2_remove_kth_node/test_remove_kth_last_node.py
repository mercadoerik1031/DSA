from typing import Optional, List
from remove_kth_last_node import remove_kth_from_end, ListNode
import pytest


# Helper functions
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

# Test cases
def test_remove_second_to_last():
    """Test removing second to last node (example case)"""
    head = create_linked_list([1, 2, 4, 7, 3])
    result = remove_kth_from_end(head, 2)
    assert linked_list_to_list(result) == [1, 2, 4, 3]

def test_remove_last_node():
    """Test removing the last node"""
    head = create_linked_list([1, 2, 3])
    result = remove_kth_from_end(head, 1)
    assert linked_list_to_list(result) == [1, 2]

def test_remove_first_node():
    """Test removing first node (when k equals length)"""
    head = create_linked_list([1, 2, 3])
    result = remove_kth_from_end(head, 3)
    assert linked_list_to_list(result) == [2, 3]

def test_single_node_list():
    """Test with a single node"""
    head = create_linked_list([1])
    result = remove_kth_from_end(head, 1)
    assert result is None

def test_empty_list():
    """Test with empty list"""
    result = remove_kth_from_end(None, 1)
    assert result is None

def test_longer_list():
    """Test with a longer list"""
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = remove_kth_from_end(head, 5)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 7, 8, 9, 10]

def test_remove_middle_node():
    """Test removing a node from the middle"""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = remove_kth_from_end(head, 3)
    assert linked_list_to_list(result) == [1, 2, 4, 5]

def test_invalid_k_too_large():
    """Test when k is larger than list length"""
    head = create_linked_list([1, 2, 3])
    with pytest.raises(ValueError):
        remove_kth_from_end(head, 4)

def test_invalid_k_zero():
    """Test when k is zero"""
    head = create_linked_list([1, 2, 3])
    with pytest.raises(ValueError):
        remove_kth_from_end(head, 0)

def test_invalid_k_negative():
    """Test when k is negative"""
    head = create_linked_list([1, 2, 3])
    with pytest.raises(ValueError):
        remove_kth_from_end(head, -1)

def test_duplicate_values():
    """Test with duplicate values to ensure we're removing the correct node"""
    head = create_linked_list([1, 2, 2, 2, 3])
    result = remove_kth_from_end(head, 3)
    assert linked_list_to_list(result) == [1, 2, 2, 3]

def test_two_node_list():
    """Test with just two nodes"""
    # Remove last node
    head1 = create_linked_list([1, 2])
    result1 = remove_kth_from_end(head1, 1)
    assert linked_list_to_list(result1) == [1]
    
    # Remove first node
    head2 = create_linked_list([1, 2])
    result2 = remove_kth_from_end(head2, 2)
    assert linked_list_to_list(result2) == [2]