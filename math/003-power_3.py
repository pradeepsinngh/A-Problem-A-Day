# Prob: Given an integer, write a function to determine if it is a power of three.

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n < 1: return False
        if n == 1: return True
        
        while n > 1:
            if n % 3 != 0:
                return False
            n = n/ 3
        
        return True
