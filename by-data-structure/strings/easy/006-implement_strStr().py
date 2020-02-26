```
# Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
```

# Sol1: 

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
        
        
# Sol2:

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

# Sol3 ;
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if haystack == needle:
            return 0
        
        if len(needle) == 0:
            return 0
        
        n = len(haystack)
        m = len(needle)
        
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        
        return -1  
        
