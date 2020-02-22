# Prob: Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        idx = 0
        return self.recur(n, idx)
    
    def recur(self, n, idx):
        
        if idx == 0:
            power2 = 1
        
        while n > power2:
            power2 = power2 * 2
            print(power2)
            
        if power2 == n:
            return True
        else:
            return False
