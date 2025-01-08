from linked_list_loop import is_loop, ListNode


def create_linked_list(values):
    head = None
    for value in reversed(values):
        node = ListNode(value)
        node.next = head
        head = node
    return head


def create_cycle(head: ListNode, pos: int):
    """Create a cycle in the linked list by connecting the last node to the node at the given position."""
    if not head or pos == -1:
        return head

    cycle_node = None
    current = head
    count = 0
    while current.next:
        if count == pos:
            cycle_node = current
        current = current.next
        count += 1

    # Connect the last node to the cycle node
    current.next = cycle_node
    return head


# -------------------- TESTS -------------------------


def test_no_cycle():
    list1 = create_linked_list([1, 2, 3, 4, 5])
    assert is_loop(list1) == False


def test_with_cycle():
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list1 = create_cycle(list1, 2)  # Creating a cycle at node with value 3
    assert is_loop(list1) == True


def test_single_node_no_cycle():
    list1 = create_linked_list([1])
    assert is_loop(list1) == False


def test_multiple_nodes_with_cycle():
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list1 = create_cycle(list1, 0)  # Creating a cycle at node with value 1
    assert is_loop(list1) == True


def test_multiple_nodes_with_cycle_from_middle():
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list1 = create_cycle(list1, 2)  # Creating a cycle at node with value 3
    assert is_loop(list1) == True


def test_empty_list():
    list1 = None
    assert is_loop(list1) == False


def test_large_list_no_cycle():
    list1 = create_linked_list(list(range(1, 10001)))  # List with 10000 nodes, no cycle
    assert is_loop(list1) == False
