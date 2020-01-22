# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # O(logn) - space
        # O(N) - time
        
        # Approach 1: Recursive method
        
        #res = []
        #if root:
        #   res = self.inorderTraversal(root.left)
        #    res.append(root.val)
        #   res = res + self.inorderTraversal(root.right)
        #return res
        
        
        # Approach 2: Iterating method using Stack
        
        # O(N) - space
        # O(N) - time
        
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
                
        return res
