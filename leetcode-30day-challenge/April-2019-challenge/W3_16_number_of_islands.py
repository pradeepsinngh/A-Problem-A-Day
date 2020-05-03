'''
# Prob: Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input:
11110
11010
11000
00000

Output: 1

'''
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
        nIslands = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    nIslands += self.bfs(row, col, grid)
        return nIslands
    
    def bfs(self, row, col, grid ):
        
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        self.bfs(row-1, col, grid)
        self.bfs(row, col-1, grid)
        self.bfs(row+1, col, grid)
        self.bfs(row, col+1, grid)
        
        return 1
        
