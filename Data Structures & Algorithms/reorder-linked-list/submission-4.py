# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #separate the lists
        s, f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        h1 = head
        h2 = s.next
        s.next = None

        #reverse the second list
        cur = h2
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        h2 = prev
        
        #merge the two lists with new head being h1
        cur = h1
        next = h2
        while cur:
            temp = cur.next
            cur.next = next
            next = temp
            cur = cur.next