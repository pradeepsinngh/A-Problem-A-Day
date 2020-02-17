# Prob: Next Greater Node In Linked List

# We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
# Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        curr = head
        stack = []
        res = []
        pos = 0
        
        while curr is not None:
            res.append(0)
            
            while stack and stack[-1][0] < curr.val:
                pop = stack.pop()
                res[pop[1]] = curr.val
        
            stack.append((curr.val, pos))
            pos += 1
            curr = curr.next
            
        return res
