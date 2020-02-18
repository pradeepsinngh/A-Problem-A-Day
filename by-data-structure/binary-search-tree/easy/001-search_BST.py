# Prob: Search in a Binary Search Tree

# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if not root:
            return None
        
        curr = root
    
        if curr.val == val:
            return curr
        
        if curr.val < val:
            return self.searchBST(curr.right, val)
        
        if curr.val > val:
            return self.searchBST(curr.left, val)
            
