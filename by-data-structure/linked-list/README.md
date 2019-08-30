## Points to remember:

1. The whole point of asking any candidates a linked list problem is to test if the candidates think about edge cases, including:
   - Dereferencing Null Pointer, usually targeting tail pointer
   - When given Head is None
   - When there are duplications in the list
   
2. The general principles for linked list manipulation is to use node operations only. 

When we are asked to solve questions related to linked list, it is widely accepted to just use just node operations and it is not allowed to change node's value. If the values of nodes are allowed to be changed, will it make sense to call this problem related to linked list? If values are allowed to be changed, why don't we solve it in the form of arrays?

3. Possible Edge cases in LinkedList:

    The linked list is empty, i.e. the head node is None.
    Multiple nodes with the target value in a row.
    The head node has the target value.
    The head node, and any number of nodes immediately after it have the target value.
    All of the nodes have the target value.
    The last node has the target value.
