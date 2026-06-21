# Allocate Minimum Pages


# In this problem, we have to minimize the maximum number of pages assigned to any student.

# So here we are checking for no. of pages b/n min(arr), sum(arr) to how many students we can assign if k then ok that can be our possible ans.



class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        
        if k > n:
            return -1
        
        si = max(arr)
        ei = sum(arr)
        
        while si <= ei:
            mid = (si+ei)//2
            
            std = self.helper(arr,mid)
            
            if std > k:
                si = mid+1
            else:
                ei = mid-1
        
        return si
    
    
    def helper(self, arr, pages):
        n = len(arr)
        std = 1
        page_allct = 0
        
        for i in range(n):
            if page_allct + arr[i] <= pages:
                page_allct += arr[i]
            else:
                std += 1
                page_allct = arr[i]
        
        return std
        
