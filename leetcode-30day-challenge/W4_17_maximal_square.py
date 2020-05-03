'''
Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


'''

class Solution:
    def maximalSquare(self, matrix):
        
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        
        dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = 0
        return max([max(row) for row in dp]) ** 2
        
