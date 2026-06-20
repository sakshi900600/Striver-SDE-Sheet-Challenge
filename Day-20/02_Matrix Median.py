# Median in a row-wise sorted Matrix


# Approach:
# The mat is row wise sorted here so we can take the min,max value as boundary
# now if suppose it will be a 1D list then mid will be at n//2. Here total elem are n+m so mid at (n*m)//2
# apply binary search and got mid
# count how many elem are less than mid , if count < req mid pos then move si else ei.
# at the end si will be pointing to mid elem.



class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Find min and max elements
        minVal = float('inf')
        maxVal = float('-inf')
        
        for i in range(n):
            minVal = min(mat[i][0], minVal)
            maxVal = max(mat[i][m-1], maxVal)
        
        
        # Required position of median (1-based index)
        req = (n * m +1) // 2
        
        # Binary search for the median
        si = minVal
        ei = maxVal
        
        while si <= ei:
            mid = (si + ei) // 2
            
            # Count elements less than or equal to mid
            count = 0
            for i in range(n):
                count += self.upperBound(mat[i], mid)
            
            if count < req:
                si = mid + 1
            else:
                ei = mid - 1
        
        return si
    
    
    def upperBound(self, arr, tar):
        n = len(arr)
        
        ans = n  # Default to n if all elements are <= tar
        si = 0
        ei = n - 1
        
        while si <= ei:
            mid = (si + ei) // 2
            
            if arr[mid] > tar:
                ans = mid
                ei = mid - 1
            else:
                si = mid + 1
        
        return ans
        
