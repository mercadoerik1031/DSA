'''
Return the head of a singly linked list after removing the kth node from the end of it.

Example:
    k = 2
    1 -> 2 -> 4 -> 7 -> 3 -> None
    
    1 -> 2 -> 4 -> 3 -> None
'''

from typing import List, Optional

class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
        

def remove_kth_from_end(head: ListNode, k: int) -> ListNode:
    if k < 1:
        return head
    
    slow = head
    fast = head
    
    while fast.next:
        if k == 0:
            slow = slow.next
            fast = fast.next
        else:
            fast = fast.next
            k -= 1
        
    slow.next = fast
    
    return head