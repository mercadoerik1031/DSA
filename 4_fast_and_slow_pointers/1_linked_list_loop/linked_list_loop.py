"""
https://leetcode.com/problems/linked-list-cycle/description/

Given a singly linked list, determine if it contains a cycle.
A cycle occurs if a node's next node pointer references an earlier node in the list, causing a loop
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def is_loop(head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Time Complexity: O(n), Space Complexity O(1)
