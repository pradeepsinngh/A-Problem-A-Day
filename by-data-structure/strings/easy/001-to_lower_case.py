# Prob: To lower case
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Sol1: 
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        return str.lower()
        
   
   
# Sol2 :
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
                
        # The ASCII codes for A-Z is 65-90 and those for a-z is that range plus 32.
        
        res = ""
        for char in str:
            if ord(char) >=65 and ord(char) <= 90:
                res += chr(ord(char)+ 32)
            else:
                res += char
        
        return res
