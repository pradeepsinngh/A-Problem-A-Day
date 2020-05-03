'''
# Prob: Game of Life
-- https://leetcode.com/problems/game-of-life/
'''

# Sol 1: 
# Space: O(m x n)
# Time: O(m x n)


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
            
                    
# Sol 2: 
# Space: O(1)
# Time: O(m x n)           
                    
                
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):

                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1

                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
                
                
