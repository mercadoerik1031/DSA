"""
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list

Example:
    1 -> 2 -> 3 -> 4 -> None
    4 -> 3 -> 2 -> 1 -> None
"""


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def reverse_linked_list(head: ListNode) -> ListNode:
    if not head:
        return

    curr = head
    nxt = None
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


# Time Complexity O(n), Space Complexity O(1)
