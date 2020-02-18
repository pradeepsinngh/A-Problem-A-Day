# Prob: Island Perimeter

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        if not grid:
            perimeter
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += 4 - (self.dfs(row, col, grid))                           
        return perimeter
    
    
    def dfs(self, row, col, grid):
        if row > 0 and grid[row-1][col] == 1:
            d = 1
        else:
            d = 0
            
        if row < len(grid)-1 and grid[row+1][col] == 1:
            b = 1
        else:
            b = 0
            
        if col > 0 and grid[row][col-1] == 1:
            a = 1
        else:
            a = 0
            
        if col < len(grid[0])-1 and grid[row][col+1] == 1:
            c = 1
        else:
            c = 0
               
        return a+b+c+d
