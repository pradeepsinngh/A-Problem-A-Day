'''
# Prob: Copy List with Random Pointer
# Clone a linked list such that each node contains an additional random pointer which could point to any node in the 
# list or null.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        hashMap = collections.defaultdict(lambda : None)
        curr = head
        
        while curr:
            if curr not in hashMap:
                hashMap[curr] = Node(curr.val, None, None)
            
            if curr.next != None:
                if curr.next not in hashMap:
                    hashMap[curr.next] = Node(curr.next.val, None, None)
                hashMap[curr].next = hashMap[curr.next]
            
            if curr.random != None:
                if curr.random not in hashMap:
                    hashMap[curr.random] = Node(curr.random.val, None, None)
                hashMap[curr].random = hashMap[curr.random]
                
            curr = curr.next
        return hashMap[head]
        
