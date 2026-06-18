# Sudoku Solver


# Checking if we can place char (1-9) or not using isvalid fun
# then filling the blank spaces in the board using the valid char and 
# if all are filled then returning true
# coz here we have to modify the board and don't return anything



class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.fillBoard(board)


    def fillBoard(self, board):

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':

                    for ch in range(1, 10):
                        if self.isValid(ch, i,j, board):
                            board[i][j] = str(ch)
                            if self.fillBoard(board):
                                return True
                            board[i][j] = '.'
                
                    return False
        
        return True
    

    def isValid(self, ch, row, col, board):
        ch = str(ch)
        
        # 1. Check row
        for i in range(9):
            if board[row][i] == ch:
                return False
        
        # 2. Check column
        for i in range(9):
            if board[i][col] == ch:
                return False
        
        # 3. Check 3x3 sub-grid
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3
        
        for r in range(box_start_row, box_start_row + 3):
            for c in range(box_start_col, box_start_col + 3):
                if board[r][c] == ch:
                    return False
        
        return True
    