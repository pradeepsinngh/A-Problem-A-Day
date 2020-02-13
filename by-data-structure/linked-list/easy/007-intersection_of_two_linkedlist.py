# Prob: Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.

## Use two pointer tech
# Time Complx: O(M+N)
# Space Complx: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        currA, currB = headA, headB
        lenA, lenB = 0,0
        
        while currA is not None:
            lenA += 1
            currA = currA.next
            
        while currB is not None:
            lenB += 1
            currB = currB.next
        
        currA, currB = headA, headB 
        
        if lenA > lenB:
            for i in range(lenA-lenB):
                currA = currA.next
                
        if lenB > lenA:
            for i in range(lenB-lenA):
                currB = currB.next
                
        while currA != currB:
            currA = currA.next
            currB = currB.next
            
        return currA
