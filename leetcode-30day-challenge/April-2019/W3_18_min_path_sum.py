'''
# Prob: Min Path Sum
'''

# Sol1 : Using DP
# Time = O(mn)
# Space = O(mn)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return
        
        rows =  len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r][c-1], grid[r-1][c])
        return grid[rows-1][cols-1]
