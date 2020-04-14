'''
# Prob: Add Two Numbers II (in a linked list)

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up: What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        sum1 = sum2 = 0
        
        while l1:
            sum1 = sum1 * 10 + l1.val
            l1 = l1.next
        while l2:
            sum2 = sum2 * 10 + l2.val
            l2 = l2.next
        
        sum = sum1 + sum2
        
        head = ListNode(0)
        if sum == 0:
            return head
        
        while sum:
            rem, sum = sum %10, sum //10
            head.next, head.next.next = ListNode(rem), head.next
        return head.next
