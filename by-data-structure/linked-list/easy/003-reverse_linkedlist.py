# Prob:  Reverse Linked List

# Sol1: Using Iterative method

# Time Complx - O(N)
# Space Complx - O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        prev = None
        next = None
        
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        self.head = prev
        
        return prev
            
            
    
# Sol 2: Using Recursion

            
            
            
            

