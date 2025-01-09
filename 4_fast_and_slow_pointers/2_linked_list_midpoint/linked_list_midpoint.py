"""
https://leetcode.com/problems/middle-of-the-linked-list/description/

Given a singly linked list, find and return its middle node.
If there are two middle nodes, return the second one.

Example 1:
    Input: 1 -> 2 -> 4 -> 7 -> 3 -> None
    Output: Node 4
    
Example 2:
    Input: 1 -> 2 -> 4 -> 7 -> None
    Output: Node 4
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


# Time Complexity: O(n), Space Complexity: O(1)
