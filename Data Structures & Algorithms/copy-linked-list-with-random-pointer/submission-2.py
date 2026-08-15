"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = collections.defaultdict(lambda: Node(0))
        hashmap[None] = None
        cur = head

        while cur:
            hashmap[cur].val = cur.val
            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur = cur.next
        
        return hashmap[head]
        


















