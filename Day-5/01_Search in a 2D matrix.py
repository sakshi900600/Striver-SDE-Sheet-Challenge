# Search in a 2D Matrix

# Approach-1:
# Simply run 2 loops and compare with all elem, if tar found then return true else false.

# Time Complexity: O(n*m)
# Space Complexity: O(1)


# Approach-2:
# given that all rows are sorted. so check in which row the tar can be present.
# Apply binary search in that row 
# return true or false accordingly.

# Time Complexity: O(n*logn)
# Space Complexity: O(1)



class Solution(object):
    def searchMatrix(self, mat, tar):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            if tar >= mat[i][0] and tar<=mat[i][m-1]:
                if self.binarySearch(mat[i], tar):
                    return True
        
        return False

    
    def binarySearch(self, arr,tar):
        n = len(arr)
        si = 0
        ei = n-1

        while si <= ei:
            mid = (si+ei)//2

            if arr[mid] == tar:
                return True
            elif arr[mid] < tar:
                si = mid+1
            else:
                ei = mid-1
        
        return False
            
        