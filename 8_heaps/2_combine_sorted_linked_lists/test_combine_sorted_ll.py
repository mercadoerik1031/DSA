from typing import List
from combine_sorted_ll import combine_sorted_linked_list, ListNode


def create_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node: ListNode) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Pytest functions


def test_empty_input():
    assert combine_sorted_linked_list([]) is None


def test_single_list():
    list1 = create_linked_list([1, 4, 5])
    result = combine_sorted_linked_list([list1])
    assert linked_list_to_list(result) == [1, 4, 5]


def test_multiple_sorted_lists_same_length():
    list1 = create_linked_list([1, 4, 6])
    list2 = create_linked_list([1, 5, 7])
    list3 = create_linked_list([2, 3, 8])
    result = combine_sorted_linked_list([list1, list2, list3])
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 5, 6, 7, 8]


def test_multiple_sorted_lists_different_length():
    list1 = create_linked_list([1, 6])
    list2 = create_linked_list([1, 4, 6])
    list3 = create_linked_list([3, 7])
    result = combine_sorted_linked_list([list1, list2, list3])
    assert linked_list_to_list(result) == [1, 1, 3, 4, 6, 6, 7]


def test_lists_with_duplicates():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([1, 2, 5])
    list3 = create_linked_list([1, 4, 6])
    result = combine_sorted_linked_list([list1, list2, list3])
    assert linked_list_to_list(result) == [1, 1, 1, 2, 3, 4, 5, 5, 6]


def test_single_element_lists():
    list1 = create_linked_list([1])
    list2 = create_linked_list([2])
    list3 = create_linked_list([3])
    result = combine_sorted_linked_list([list1, list2, list3])
    assert linked_list_to_list(result) == [1, 2, 3]
