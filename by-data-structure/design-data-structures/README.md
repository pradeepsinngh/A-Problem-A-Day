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

#### Declaring a list 
L = [1, "a" , "string" , 1+2] 

#### add 6 to the above list 
L.append(6) 
  
#### pop deletes the last element of the list 
L.pop()   
print L[1] 

## Dictionary
- In python, Dictionary is similar to hash or maps in other languages. 
- It consists of key value pairs. 
- The value can be accessed by unique key in the dictionary.
- Keys are unique & immutable objects.

Syntax: dictionary = {"key name": value}

```
#### Create a new dictionary  
d = dict() # or d = {} 
  
#### Add a key - value pairs to dictionary 
d['xyz'] = 123
d['abc'] = 345
  
#### print the whole dictionary 
print d 
  
#### print only the keys 
print d.keys() 
  
#### print only values 
print d.values() 
  
#### iterate over dictionary  
for i in d : 
    print "%s %d" %(i, d[i]) 
  
#### another method of iteration 
for index, value in enumerate(d): 
    print index, value , d[value] 
  
#### check if key exist 
print 'xyz' in d 
  
#### delete the key-value pair 
del d['xyz'] 
  
#### check again  
print "xyz" in d 
```
