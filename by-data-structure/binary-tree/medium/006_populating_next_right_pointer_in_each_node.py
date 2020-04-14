```
# Prob: Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer 
should be set to NULL.

Initially, all next pointers are set to NULL.
```


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
        
        if root and root.left and root.right:
            root.left.next = root.right
            
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        
        return root
