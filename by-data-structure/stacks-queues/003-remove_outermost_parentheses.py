# Prob: Remove Outermost Parentheses
# Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.


# Sol1: Using stack

Time Complx: O(m + n)
Space Complx: O(m + n)

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def build(S):
            res = []
            for c in S:
                if c != '#':
                    res.append(c)
                elif res:
                    res.pop()
            return ''.join(res)
        
        return build(S) == build(T)
