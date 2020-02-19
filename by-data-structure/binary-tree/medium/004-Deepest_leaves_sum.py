# Prob : Given a binary tree, return the sum of values of its deepest leaves. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        res = {}
        self.dfs(root, count, res)
        
        return res[max(res)]
        
        
    def dfs(self, root, count, res):
        if root:
            if count not in res:
                res[count] = root.val
            else:
                res[count] += root.val
            self.dfs(root.left, count+1, res)
            self.dfs(root.right, count+1, res)
        
        return res
