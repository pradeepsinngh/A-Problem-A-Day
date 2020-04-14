'''
# Prob: Clone Graph

'''

# Sol1 : Recursive using DFS
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        hashMap = {}
        return self.dfs(node, hashMap)
        
    def dfs(self, node, dic):
        if not node:
            return
        else:
            dic[node] = Node(node.val, [])
            for n in node.neighbors:
                if n in dic:
                    dic[node].neighbors.append(dic[n])
                else:   
                    dic[node].neighbors.append(self.dfs(n, dic))
            return dic[node]
        
        
        
            
        
