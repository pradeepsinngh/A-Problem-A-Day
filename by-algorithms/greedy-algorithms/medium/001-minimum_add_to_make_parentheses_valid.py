# Prob: Minimum Add to Make Parentheses Valid

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        # greedy approach
        
        bal = 0
        ans = 0
        
        for symbol in S:
            if symbol == "(":
                bal += 1
            else:
                bal -= 1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
