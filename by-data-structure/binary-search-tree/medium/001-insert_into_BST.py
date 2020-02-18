# Prob:  Insert into a Binary Search Tree

# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        head = root
        self.binarySearch(root, val)
        
        return head
        
                
    def binarySearch(self, root, val):
        
        currVal = root.val
        
        if currVal < val:
            if not root.right:
                newNode = TreeNode(val)
                root.right = newNode
                return 
            else:
                self.binarySearch(root.right, val)
                
        if currVal > val:
            if not root.left:
                newNode = TreeNode(val)
                root.left = newNode
                return
            else:
                self.binarySearch(root.left, val)
