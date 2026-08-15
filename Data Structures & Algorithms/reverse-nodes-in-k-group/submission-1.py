# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group = 0
        cur = head
        while group < k:
            if cur:
                cur = cur.next
            else:
                return head
            group += 1
        next_part = self.reverseKGroup(cur, k)
        prev = next_part
        cur = head
        for i in range(k):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        

        return prev
