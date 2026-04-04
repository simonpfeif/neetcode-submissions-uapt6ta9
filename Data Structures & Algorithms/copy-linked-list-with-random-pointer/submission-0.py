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
        hash = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hash[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            hash[cur].random = hash[cur.random]
            hash[cur].next = hash[cur.next]
            cur = cur.next

        return hash[head]