"""
Given k singly linked lists, each sorted in ascending order, combine them into one sorted linked list

Example:
    Input:
        1 -> 6
        1 -> 4 -> 6
        3 -> 7
    
    Output: 1 -> 1 -> -> 3 -> 4 -> 6 -> 6 -> 7
"""

import heapq
from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


def combine_sorted_linked_list(lists: List[ListNode]) -> ListNode:
    min_heap = []
    dummy_head = ListNode(-1)
    curr = dummy_head

    for head in lists:
        heapq.heappush(min_heap, head)

    while min_heap:
        smallest_node = heapq.heappop(min_heap)
        curr.next = smallest_node
        curr = curr.next

        if smallest_node.next:
            heapq.heappush(min_heap, smallest_node.next)

    return dummy_head.next


# Time Complexity: O(n log(k)), Space Complexity: O(k)
