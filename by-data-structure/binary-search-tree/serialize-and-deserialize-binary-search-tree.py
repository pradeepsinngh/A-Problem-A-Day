# Prob: Serialize and Deserialize BST


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        vals = []
        vals = self.preOrder(root, vals)
        print(vals)
        return ' '.join(vals)
    
    def preOrder(self, root, vals):
        
        if root:
            vals.append(str(root.val))
            self.preOrder(root.left, vals)
            self.preOrder(root.right, vals)
        else:
            vals.append('#')
        
        return vals


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        return self.helper(data, vals)
    
    def helper(self, data, vals):
        val = next(vals)
        if val == '#':
            return None
        
        Node = TreeNode(int(val))
        Node.left = self.helper(data, vals)
        Node.right = self.helper(data, vals)
        return Node
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
