# Max Area of Island:

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        maxArea = []
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea.append(self.dfs(grid, row, col))
        
        if len(maxArea) == 0:
            return 0
        else:
            Area = max(maxArea)           
        return Area
    
    def dfs(self, grid, row, col):
        sum = 0
        if row< 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        
        sum += grid[row][col]
        grid[row][col] = 0
        sum += self.dfs(grid, row-1, col)
        sum += self.dfs(grid, row, col-1)
        sum += self.dfs(grid, row+1, col)
        sum += self.dfs(grid, row, col+1)
        
        return sum
