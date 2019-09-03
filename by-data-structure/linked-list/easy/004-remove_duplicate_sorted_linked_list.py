# Prob: Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Sol1: 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        current = head.next
        prev = head
        
        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
                
        return head
        
        
        
        
        
        
        
        
        
