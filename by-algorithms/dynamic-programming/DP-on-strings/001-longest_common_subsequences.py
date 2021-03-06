'''
# Prob: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.

Example:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''

# Sol 1: Using DP

# Time and Space : O(m * n)

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                if c == d:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max( dp[i][j+1], dp[i+1][j] )
        return dp[-1][-1]
