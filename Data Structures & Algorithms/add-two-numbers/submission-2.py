# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            if l1 is not None:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2 is not None:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            sum = num1 + num2 + carry
            carry, res = divmod(sum, 10)

            cur.next = ListNode(res)
            cur = cur.next

        return dummy.next







