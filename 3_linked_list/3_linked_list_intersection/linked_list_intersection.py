"""
https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1502164968/

Return the node where two singly linked lists intersect. If the linked lists don't intersect,
return null
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def find_intersection(
    head1: Optional[ListNode], head2: Optional[ListNode]
) -> Optional[ListNode]:

    curr1 = head1
    curr2 = head2

    while curr1 != curr2:
        curr1 = curr1.next if curr1 else head2
        curr2 = curr2.next if curr2 else head1

    return curr1


# Time Complexity: O(n + m), Space Complexity: O(1)
# n = length of list1, m = length of list2
