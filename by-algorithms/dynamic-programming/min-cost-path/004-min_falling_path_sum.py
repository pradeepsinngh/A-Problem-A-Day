'''
# Prob: Minimum Falling Path Sum
# Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.


Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

'''


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for c in range(cols):
            dp[0][c] = A[0][c]
            
        for r in range(1,rows):
            for c in range(cols):
                
                if c == 0:
                    dp[r][0] = A[r][c] + min(dp[r-1][c], dp[r-1][c+1])
                elif c == (cols-1):
                    dp[r][c] = A[r][c] + min(dp[r-1][c], dp[r-1][c-1])
                else:
                    dp[r][c] = A[r][c] + min(dp[r-1][c], dp[r-1][c-1], dp[r-1][c+1])
                    
        return min(dp[rows-1][:])
                
                
                    
                
                
                
        
        
