# Prob: Rotting Oranges


class Solution:
    def orangesRotting(self, grid):
        
        R, C = len(grid), len(grid[0])
        
        # Get location of all rotten oranges
        q = []
        for r in range(R):
             for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        # BFS
        total_time = 0
        for r, c, time in q:
            if grid[r][c] != 0:
                grid[r][c] = 0
                total_time = max(total_time, time)    
                
                # Added 4 directions
                for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= x < R and 0 <= y < C and grid[x][y] == 1:
                        q.append((x, y, time+1))
        

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    return -1
                
        return total_time
