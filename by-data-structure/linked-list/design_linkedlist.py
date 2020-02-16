class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None 
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        current = self.head
        
        for i in range(index):
            if i == n:
                if current is None:
                    return -1
                else:
                    return current
            
            current = current.next

            
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        
        current = self.head
        
        newNode = Node(val)
        current = newNode.next
        newNode = self.head
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        
        current = self.head
        newNode = Node(val)
        
        if current is None:
            current = newNode
        else:
            while current.next is not None:
                current = current.next
                
            current.next = newNode
        #newNode.next = NULL
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        if index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
                
            node = Node(val)
            node.next = current.next
            current.next = node


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        
        current = self.head
        
        if index == 0:
            self.head = current.next
        else:
            for i in range(index-1):
                current = current.next
                
            current.next = current.next.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
