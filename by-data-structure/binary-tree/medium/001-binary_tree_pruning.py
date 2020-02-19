# Prob: Binary Tree Pruning
# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val:
            return root
        else:
            if root.left or root.right:
                return root 
            else:
                return None
