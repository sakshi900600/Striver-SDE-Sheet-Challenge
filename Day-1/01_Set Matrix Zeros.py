# Set Matrix Zeros:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


# Logic:
# We have to somehow rem which row & col has 0, so that we can mark that whole row&col to 0.

# To do it: I took 2 arr. One for marking row and another for col.
# Then traversed the mat and mark both array.

# Finally, If there is any 0 in any row or col then put 0 in the whole row and col of original given mat. 

# Time Complexity: O(n*m)
# Space Complexity: O(n+m) for markr and markc arrays


class Solution(object):
    def setZeroes(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        m = len(mat[0])
        
        markr = [0]*n
        markc = [0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    markr[i] = 1
                    markc[j] = 1
        
        for i in range(n):
            if markr[i] == 1:
                # change all elem of this row to 0
                for j in range(m):
                    mat[i][j] = 0
        
        for j in range(m):
            if markc[j] == 1:
                # change all elem of this col to 0
                for i in range(n):
                    mat[i][j] = 0
        
        

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    print(matrix)

