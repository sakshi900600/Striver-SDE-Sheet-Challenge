# Minimum Platforms



class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        trains = []
        
        for i in range(len(arr)):
            trains.append((arr[i], dep[i]))
            
        trains.sort()
        
        dct = {}
        dct[0] = trains[0][1]
        
        count = 1
        
        for train in trains[1:]:
            a = train[0]
            d = train[1]
            
            val = self.helper(dct, a)
            
            if val != -1:
                dct[val] = d
            else:
                dct[count] = d
                count += 1
                
        return count
        
        
    def helper(self, dct, a):
        
        for k,v in dct.items():
            if a > v:
                return k
        return -1
        
        

# Optimized Approach:

import heapq
class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        trains = []
        
        for i in range(len(arr)):
            trains.append((arr[i], dep[i]))
            
        trains.sort()
        
        pq = []
        heapq.heappush(pq, trains[0][1])
        
        count = 1
        
        for train in trains[1:]:
            a = train[0]
            d = train[1]
            
            # if curr arrival > last min dept time
            if pq and a > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, d)
            else:
                count += 1
                heapq.heappush(pq, d)
            
        return count
        

        
        