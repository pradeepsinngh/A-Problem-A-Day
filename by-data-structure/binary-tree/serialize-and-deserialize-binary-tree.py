# PRob: Serialize and Deserialize Binary Tree


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
        def doit():
            val = next(vals)
            if val == '#':
                return None
            
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        
        vals = iter(data.split())
        return doit()
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
