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

        hashMap = {None : None}
        cur = head
        
        while cur:
            copy = Node(cur.val)
            hashMap[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = hashMap[cur]
            copy.next = hashMap[cur.next]
            copy.random = hashMap[cur.random]
            cur = cur.next
        
        return hashMap[head]