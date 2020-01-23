# Problem: Odd Even Linked List

# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Sol 1:

# Time: O(N), where N are number of nodes.
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return
        
        odd = head
        even = odd.next
        tmp_node = odd.next
        
        while odd.next and even.next:
            odd.next = odd.next.next
            #if odd.next:
            odd = odd.next
            even.next = even.next.next
            even = even.next 
            
        odd.next = tmp_node
        return head
