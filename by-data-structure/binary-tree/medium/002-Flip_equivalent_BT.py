# Prob: Flip Equivalent Binary Trees

# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
# Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)))
