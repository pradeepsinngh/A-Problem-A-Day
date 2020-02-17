# Prob: Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array. 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        q = collections.deque()
        res = []
        
        if not root:
            return []
        
        if root:
            q.append(root)
            
        while len(q):
            level_sum = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level_sum.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(level_sum)
            
        ans = []
        for l in res:
            avg = sum(l) * 1.0 / (len(l))
            ans.append(avg)
        
        return ans
