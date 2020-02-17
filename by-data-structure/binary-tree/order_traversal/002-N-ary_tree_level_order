# Prob: N-ary Tree Level Order Traversal
# Given an n-ary tree, return the level order traversal of its nodes' values.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        q = collections.deque()
        res = []
        
        if not root:
            return []
        
        if root:
            q.append(root)
            
        while len(q):
            level = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)
                
                if curr.children:
                    for child in curr.children:
                        q.append(child)
                
            res.append(level)
            print(res)
        return res
