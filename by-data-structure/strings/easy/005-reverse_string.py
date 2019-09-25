```
Reverse String: 

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

```

# Sol 1: Two pointer approach

Time Complx: O(n)
Space Complx: O(1)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        l = len(s)-1
    
        for i in range(len(s)//2):
            left = s[i]
            right = s[l-i]
            s[i] = right
            s[l-i] = left
            
        return s
        
        
# Sol2: Traverse through a list and append all elements of list backwards to another list.

Time Complx: O(n)
Space Complx: O(n)
