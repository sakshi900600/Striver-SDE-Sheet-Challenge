# Pascal's Triangle:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


# Approach: 
# we need to return list of list or matrix. The rows in mat = numRows and in each row the no. of elem is (rowno + 1)

# start and last value in each row is 1. 

# rest elem value is calculated by taking the val of (upper left corner elem + top elem) value.

# Time Complexity: O(numRows^2) as we are traversing the matrix of size numRows * numRows

# Space Complexity: O(numRows^2)


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        for i in range(numRows):
            li = []
            for j in range(i+1):
                if i==j or j==0:
                    li.append(1)
                else:
                    val = ans[i-1][j-1] + ans[i-1][j]
                    li.append(val)

            ans.append(li)
        
        return ans
        
        

if __name__ == "__main__":
    sol = Solution()

    numRows = 5
    print(sol.generate(numRows))
