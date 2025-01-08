"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Return the head of a singly linked list after removing the kth node from the end of it.

Example:
    k = 2
    1 -> 2 -> 4 -> 7 -> 3 -> None
    
    1 -> 2 -> 4 -> 3 -> None
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def remove_kth_from_end(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None

    if k < 1:
        raise ValueError

    dummy = ListNode(-1)
    dummy.next = head
    slow = dummy
    fast = head

    for _ in range(k):
        if not fast:
            raise ValueError
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


# Time Complexity: O(n), Space Complexity: O(1)
