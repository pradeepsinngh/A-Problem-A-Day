# Prob: Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            if board[row][0] == 'O':
                self.dfs(row, 0, board)
            if board[row][cols-1] == 'O':
                self.dfs(row, cols-1, board)
                
        for col in range(cols):
            if board[0][col] == 'O':
                self.dfs(0, col, board)
            if board[rows-1][col] == 'O':
                self.dfs(rows-1, col, board)
                
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '*':
                    board[row][col] = 'O' 
        
        return board
        
    def dfs(self, row, col, board):
        
        if row< 0 or col<0 or row> len(board)-1 or col >len(board[0])-1 or board[row][col] != 'O':
            return
        
        if board[row][col] == 'O':
            board[row][col] = '*'
        self.dfs(row-1,col, board)
        self.dfs(row, col-1, board)
        self.dfs(row+1, col, board)
        self.dfs(row,col+1, board)
        
