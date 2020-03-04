# Prob: Diameter of a Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        self.dfs(root)
        return self.res
    
    
    def dfs(self, node):
        if not node:
            return 0
        
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        self.res = max(self.res, L+R)
        return max(L,R)+1
    
