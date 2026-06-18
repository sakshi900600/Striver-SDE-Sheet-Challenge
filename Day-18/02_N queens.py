# N Queens


# We are filling queens row wise...
# Here checking if we can place queen or not using issafe fun
# The writing a recursive code there
# if successfully filled last row then store the solution
# Exploring for each row and filling if safe and backtracking to explore all possiblities
# In the main fun returning list of all pos solutions


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        mat = [['.']*n for _ in range(n)]

        self.placeQueens(0,mat, ans)
        return ans


    def placeQueens(self, row, mat, ans):
        n = len(mat)

        li = []
        if row == n:
            for i in range(n):
                s = "".join(mat[i])
                li.append(s)

            ans.append(li)
            return
        
        for col in range(n):
            if self.isSafe(row, col, mat):
                mat[row][col] = 'Q'
                self.placeQueens(row+1, mat, ans)
                mat[row][col] = '.'
    
    
    def isSafe(self, row, col, mat):
        n = len(mat)
        r = row
        c = col

        # col
        for i in range(row):
            if mat[i][col] == 'Q':
                return False
        
        # diagonal left
        r = row-1
        c = col-1
        while r >= 0 and c >= 0:
            if mat[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        # diagonal right
        r = row-1
        c = col+1
        while r>=0 and c <n:
            if mat[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True



        