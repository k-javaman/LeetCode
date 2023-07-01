# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        if p.val < cur.val and q.val < cur.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        if p.val > cur.val and q.val > cur.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        else:
            return root
                
    

            
            