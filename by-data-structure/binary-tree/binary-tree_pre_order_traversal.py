# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Time: O(logn)
        # Space: O(N)
        
        #res = []
        #if root:
        #    res.append(root.val)
        #    res = res + self.preorderTraversal(root.left)
        #    res = res + self.preorderTraversal(root.right)
        #else:
        #    return []
        
        #return res
        
        res, stack = [], [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return res
