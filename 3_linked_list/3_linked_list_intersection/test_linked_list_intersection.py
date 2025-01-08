from linked_list_intersection import find_intersection, ListNode


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = None
    for value in reversed(values):
        node = ListNode(value)
        node.next = head
        head = node
    return head


# Test Case 1: Two linked lists intersect at a node
def test_lists_intersect():
    # Create two lists that intersect at node 8
    common = ListNode(8)
    common.next = ListNode(10)

    list1 = ListNode(3)
    list1.next = ListNode(7)
    list1.next.next = common

    list2 = ListNode(99)
    list2.next = ListNode(1)
    list2.next.next = common

    intersection_node = find_intersection(list1, list2)
    assert intersection_node is not None
    assert intersection_node.val == 8


# Test Case 2: Two linked lists do not intersect
def test_lists_dont_intersect():
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])

    intersection_node = find_intersection(list1, list2)
    assert intersection_node is None


# Test Case 3: One of the linked lists is empty
def test_one_list_is_empty():
    list1 = create_linked_list([1, 2, 3])
    list2 = None

    intersection_node = find_intersection(list1, list2)
    assert intersection_node is None


# Test Case 4: Both linked lists are empty
def test_both_lists_empty():
    list1 = None
    list2 = None

    intersection_node = find_intersection(list1, list2)
    assert intersection_node is None


# Test Case 5: Intersection happens at the head of the list
def test_intersection_at_head():
    common = ListNode(1)
    list1 = common
    list2 = common

    intersection_node = find_intersection(list1, list2)
    assert intersection_node is not None
    assert intersection_node.val == 1


# Test Case 6: Intersection happens at a middle node
def test_intersection_at_middle():
    common = ListNode(8)
    common.next = ListNode(10)

    list1 = ListNode(3)
    list1.next = ListNode(7)
    list1.next.next = common

    list2 = ListNode(99)
    list2.next = ListNode(1)
    list2.next.next = common

    intersection_node = find_intersection(list1, list2)
    assert intersection_node is not None
    assert intersection_node.val == 8
