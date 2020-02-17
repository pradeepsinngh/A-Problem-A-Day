# BFS: Traverse a tree by level order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        q = collections.deque()
        res = []
        
        if not root:
            return []
        
        if root:
            q.append(root)
            
        while (len(q)):
            level = []
            
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            res.append(level)
        return res
