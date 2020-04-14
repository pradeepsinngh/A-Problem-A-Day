'''
# Prob: Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer 
should be set to NULL.

Initially, all next pointers are set to NULL.
'''

## -----------------------
# Sol 1: Using Recursive Approach

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root and root.left and root.right:
            root.left.next = root.right
            
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        
        return root


## -----------------------
# Sol 2: DFS (Using stack

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # DFS (using stack)
        if not root:
            return
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)
        return root
        
        
### ------------    
# Sol 3: BFS (using queue)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # BFS (using stack)
        
        if not root:
            return
        
        q = [root]
        
        while q:
            curr = q.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                q.append(curr.left)
                q.append(curr.right)
                
        return root
        
