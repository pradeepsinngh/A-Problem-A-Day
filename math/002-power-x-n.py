# Prob : Implement pow(x, n), which calculates x raised to the power n (xn).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n = n //2
        return res
