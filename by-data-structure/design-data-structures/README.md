# Inbuilt Data Structures:

Python has four basic inbuilt data structures namely:
 - Lists, 
 - Dictionary, 
 - Tuple and 
 - Set.

## List

- Lists can be used for any type of object, from numbers and strings to more lists.
- They are accessed just like strings (e.g. slicing and concatenation) so they are simple to use and they’re variable length, i.e. they grow and shrink automatically as they’re used.
- In reality, Python lists are C arrays inside the Python interpreter and act just like an array of pointers.
- There are various Functions that can be carried out on lists like *append(), extend(), reverse(), pop()* etc.

# Python program to illustrate 
# A simple list 
  
# Declaring a list 
L = [1, "a" , "string" , 1+2] 

# add 6 to the above list 
L.append(6) 
  
# pop deletes the last element of the list 
L.pop()   
print L[1] 
