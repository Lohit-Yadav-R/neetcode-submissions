# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        cur = head
        next = prev
        while cur:
            nextnode = next
            next = cur.next
            cur.next = nextnode
            cur = cur.next




