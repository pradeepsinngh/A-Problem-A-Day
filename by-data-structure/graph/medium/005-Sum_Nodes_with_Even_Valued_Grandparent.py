Prob: Sum of Nodes with Even-Valued Grandparent
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        if not root:
            return res
        
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        
        if not root:
            return
        
        if root.val % 2 == 0:
            if root.left and root.left.left:
                self.res += root.left.left.val
                
            if root.left and root.left.right:
                self.res += root.left.right.val
            
            if root.right and root.right.left:
                self.res += root.right.left.val
                
            if root.right and root.right.right:
                self.res += root.right.right.val
            
        self.dfs(root.left)
        self.dfs(root.right)
