# Prob: Kth smallest element in BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        res = []
        self.inOrder(root, res)
        return res[k-1]
        
        
    def inOrder(self, root, res):
        
        if not root:
            return
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
                
        return res
