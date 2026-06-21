# Agressive Cows:

# In this problem, we have to return minimum distance between any two of stalls is the maximum possible

# Here instead of placing cows on stall and getting distance
# We are checking if for a particular distance we can place all k cows or not.



class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        n = len(stalls)
        stalls.sort()
        
        si = 1
        ei = stalls[-1]-stalls[0]
        
        ans = -1
        
        while si <= ei:
            mid = (si+ei)//2
            
            if self.ispossible(stalls,mid,k):
                ans = mid
                si = mid+1
            else:
                ei = mid-1
        
        return ans
    
    
    def ispossible(self, arr,dist,k):
        n = len(arr)
        cowcnt = 1
        last = arr[0]
        
        for i in range(1,n):
            if arr[i]-last >= dist:
                cowcnt += 1
                last = arr[i]
                
                if cowcnt == k:
                    return True
        
        return False
    
    