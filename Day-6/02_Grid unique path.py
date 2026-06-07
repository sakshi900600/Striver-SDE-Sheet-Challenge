# Grid Unique Path counts


# Approach -1:
# First I try to solve it using recursion. 
# so i worte a fun and the base condition is when row,col ==m-1,n-1 then I return 1

# I checked if issafe i.e. row>=m or col>=n then return 0
# I called for both moves right and down
# at the end i call this helper fun inside the main fun and returned 
# gives tle .>>>>


# Approach -2 :
# Memoized this soution using 2d dp. 



class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[-1]*n for _ in range(m)]
        
        return self.helper(0,0,m,n,dp)
        

    def helper(self,row, col, m,n,dp):
        if row==m-1 and col==n-1:
            return 1
            
        if row >= m or col >= n:
            return 0

        if dp[row][col] != -1:
            return dp[row][col]

        right = self.helper(row, col+1,m,n,dp)
        down = self.helper(row+1,col, m,n,dp)
        dp[row][col] = right + down

        return dp[row][col]
            
