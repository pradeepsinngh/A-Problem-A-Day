# Problem: Implement Post Order Traversal for a binary search tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Approach 1: Recurisve
        
        #res = []
        #if root:
        #    res = res + self.postorderTraversal(root.left)
        #    res = res + self.postorderTraversal(root.right)
        #    res.append(root.val)
        #else:
        #    return []
        
        #return res
        
        # Approach 2: Modified Pre Order
        
        #res = []
        #stack = []
        #current = root
        
        # pre-order, right first and then left
        #while stack or current:
        #    if current:
        #        stack.append(current)
        #        res.append(current.val)
        #        current = current.right
        #    else:
        #        current = stack.pop()
        #        #res.append(current.val)
        #        #current = stack.pop()
        #        current = current.left
                
        #return res[::-1]
        
        
        # Approach 3: Use Flag to keep track of visited node
        
        res = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                
        return res
            
        
