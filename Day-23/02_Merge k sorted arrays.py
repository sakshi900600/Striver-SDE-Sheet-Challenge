# Merge k Sorted Arrays

# Approach:
# Just like we merge 2 sorted list by taking 2 variables for both array, here we are using col as that variable and everytime whatever the min value we got move next elem in the same row, next column.



import heapq
class Solution:
    def mergeArrays(self, mat):
        # Code here
        
        n = len(mat)
        m = len(mat[0])
        
        pq = []
        ans = []
        
        for i in range(n):
            heapq.heappush(pq, (mat[i][0], i,0))
        
        
        while pq:
            val, r,c = heapq.heappop(pq)
            ans.append(val)
            
            if c+1 < m:
                heapq.heappush(pq, (mat[r][c+1], r, c+1))
            
        
        return ans
            