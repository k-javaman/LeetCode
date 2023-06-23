# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If root is None, return 0 as depth
        if not root:
            return 0

        # Initialize level to 0
        level = 0
        # Initialize queue with root node
        # q = deque([root]) creates a new deque (which is like a double-ended queue) and initializes it with the root node of the tree.
        q = deque([root])
        # Process until the queue is empty
        while q:
            # For each level, iterate over all the nodes
            for i in range(len(q)):
                # Pop a node from the front of the queue
                node = q.popleft()
                # If left child exists, add it to the queue
                if node.left:
                    q.append(node.left)
                # If right child exists, add it to the queue
                if node.right:
                    q.append(node.right)

            # After each level is processed, increment level count
            level += 1
        # Return the total levels processed which is the depth of the tree
        return level