'''
# Prob: Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. 
You may assume that the maximum length of s is 1000.

Example:
Input: "bbbab"
Output: 4

'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            dp[i][i] = 1
            
        for i in range(N-1):
            dp[i][i+1] = 2 if s[i]==s[i+1] else 1
            
        for dis in range(2, N):
            for i in range(0, N-dis):
                j = i+dis
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max( dp[i+1][j], dp[i][j-1] )
                    
        return dp[0][N-1]
