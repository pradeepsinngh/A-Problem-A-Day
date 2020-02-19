# Prob: Vertical Order Traversal of a Binary Tree

# Given a binary tree, return the vertical order traversal of its nodes values.
# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        dic = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0, 0))
        ans = []
        
        while q:
            for _ in range(len(q)):
                node, hd, vd = q.popleft()
                dic[hd].append((vd,node.val))
                if node.left:
                    q.append((node.left, hd-1, vd-1))
                if node.right:
                    q.append((node.right, hd+1, vd-1))
        
        
        for i in sorted(dic.keys()):
            level = []
            for x in sorted((dic[i]), key=lambda x:(-x[0],x[1])):
                level.append(x[1])
            ans.append(level)
        return ans
