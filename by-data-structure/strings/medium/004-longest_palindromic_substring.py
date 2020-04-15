'''
# Prob: Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

'''
# Sol1 : Brute Force:
# For every (palindromic) substring in a string, keep track of max len.

# Time Complx - O(N3) - Three for loops, two for finding substrings and 1 for finding palindromic substring
# Space Complx - O(N) - Where N are number of substrings


# Sol2 : Expand Around Center

# Time complx - O(N2)
# Space Complx - O(1)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        n = len(s)
        for i in range(n):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+1)
            res = max(odd, even, res, key=len)
        return res
    
    def helper(self, s, left, right):
        
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return s[left+1:right]
