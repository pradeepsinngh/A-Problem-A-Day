# Prob: Repeated Substring Pattern

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the 
# substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 
# 10000.


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        return s in (s+s)[1:-1]
