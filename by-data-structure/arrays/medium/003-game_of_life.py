'''
# Prob: Game of Life
-- https://leetcode.com/problems/game-of-life/
'''


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        copy = [[board[row][col] for col in range(cols)] for row in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                
                live_neigh = 0
                
                for neigh in neighbors:
                    r = row + neigh[0]
                    c = col + neigh[1]
                    
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy[r][c] == 1):
                        live_neigh += 1
                
                # rule 1
                if copy[row][col] == 1 and (live_neigh < 2 or live_neigh > 3):
                    board[row][col] = 0
                    
                if copy[row][col] == 0 and live_neigh == 3:
                    board[row][col] = 1
            
                    
                
                    
                        
                
                
