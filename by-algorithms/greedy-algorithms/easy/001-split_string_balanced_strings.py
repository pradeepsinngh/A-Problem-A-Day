# Prob: Split a String in Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        R_count = 0
        L_count = 0
        Bal_count = 0
        
        for char in s:
            if char == "R":
                R_count += 1
            else:
                L_count += 1
            if R_count == L_count:
                Bal_count += 1
        return Bal_count
