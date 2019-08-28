# Prob: Middle of the Linked List
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

Link -- https://leetcode.com/problems/middle-of-the-linked-list/

# Sol1: Two Pointers:

# Time Complx: O(N)
# Space Complx: O(N)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        fast_pointer = head
        slow_pointer = head
        
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            
        return slow_pointer
        
    
 # Sol 2: Iterate through linkedlist, compute length, return l-n node
 
