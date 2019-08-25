# Prob: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is 
# the sum of the two preceding ones, starting from 0 and 1. That is,

# Given N, calculate F(N).

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)
