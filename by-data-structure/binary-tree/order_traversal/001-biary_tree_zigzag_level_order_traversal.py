# Prob: Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        q = collections.deque()
        res = []
        
        if not root:
            return []
        
        if root:
            q.appendleft(root)
            
        zigzag = False
        
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                if zigzag:
                    curr = q.pop()
                    level.append(curr.val)
                    if curr.right:
                        q.appendleft(curr.right)
                    if curr.left:
                        q.appendleft(curr.left)
                else:
                    curr = q.popleft()
                    level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
            res.append(level)
            zigzag = not zigzag
            
        return res
