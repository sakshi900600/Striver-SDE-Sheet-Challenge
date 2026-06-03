# Rotate matrix by 90 degree
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


# Approach: 
# I have first transposed the matrix and then reversed each row to get the desired output.

# the inner loop start from i+1 not i because if we start from i then we will swap the elements twice and we will get the original matrix as output instead of rotated matrix.


# Time Complexity: O(n^2) for transposing and O(n^2) for reversing each row. Overall O(n^2)
# Space Complexity: O(1) as we are modifying the matrix in-place.



class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

        
