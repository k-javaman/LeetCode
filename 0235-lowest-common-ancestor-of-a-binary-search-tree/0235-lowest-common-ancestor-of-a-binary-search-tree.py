# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This class represents a solution for finding the lowest common ancestor in a binary search tree
# This class represents a solution for finding the lowest common ancestor in a binary search tree
class Solution:
    # The method lowestCommonAncestor receives a root node and two other nodes p and q and finds their
    # lowest common ancestor in the binary search tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       cur = root
       
       while cur:
           if p.val > cur.val and q.val > cur.val:
               cur = cur.right
           elif p.val < cur.val and q.val < cur.val:
               cur = cur.left
           else:
               return cur

            
            