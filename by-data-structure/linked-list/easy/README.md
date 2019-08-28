## Points to remember:

1. The whole point of asking any candidates a linked list problem is to test if the candidates think about edge cases, including:
   - Dereferencing Null Pointer, usually targeting tail pointer
   - When given Head is None
   - When there are duplications in the list
   
2. The general principles for linked list manipulation is to use node operations only. 

When we are asked to solve questions related to linked list, it is widely accepted to just use just node operations and it is not allowed to change node's value. If the values of nodes are allowed to be changed, will it make sense to call this problem related to linked list? If values are allowed to be changed, why don't we solve it in the form of arrays?
