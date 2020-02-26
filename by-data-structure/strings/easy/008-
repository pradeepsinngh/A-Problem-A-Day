# Prob: Word Pattern
# Given a pattern and a string str, find if str follows the same pattern.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        s = pattern
        t = str.split()
        
        if len(s) != len(t):
            return False
        
        if map(s.find, s) == map(t.index, t):
            return True
        else:
            return False
