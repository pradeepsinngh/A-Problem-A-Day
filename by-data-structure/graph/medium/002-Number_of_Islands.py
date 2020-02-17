# Prob: Number of Islands:

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        numIslands = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    numIslands += self.dfs(grid, row, col)
                    
        return numIslands
    
    
    def dfs(self, grid, row, col):

        if (row<0 or row >= len(grid) or col<0 or col >= len(grid[0]) or grid[row][col] == '0'):
            return 0
            
        grid[row][col] = '0'
        self.dfs(grid, row-1, col)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row, col+1)
            
        return 1
