# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(cur, prev):
            if cur is None:
                return prev
            else:
                nxt = cur.next
                cur.next = prev
                return recursive(nxt, cur)
            
        return recursive(head, None)
            
        
            
        
        
            

