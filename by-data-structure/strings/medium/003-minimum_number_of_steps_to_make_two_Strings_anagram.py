# Prob: Minimum Number of Steps to Make Two Strings Anagram

# Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        count = collections.Counter(s)
        res = 0
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                res += 1
                
        return res
