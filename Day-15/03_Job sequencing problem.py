# Job Sequencing Problem


# Approach:
# Here we are trying to finish as much job as we can with maxm profit.


# T.C = O(nlong)
# S.C = O(n + maxd)


class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        
        maxProfit = 0
        count = 0
        
        # create jobs pair
        jobs = []
        for i in range(len(profit)):
            j = deadline[i]
            p = profit[i]
            
            newJob = (j,p)
            jobs.append(newJob)
            
        
        # find max deadline so that we can add jobs in slots.
        max_deadline = max(deadline)
        
        # i am creating +1 extra size but i will never use 0th index. its just to sync deadline and index value.
        arr = [0]*(max_deadline+1)
        
        # sort job based on profit
        jobs.sort(key=lambda x: x[1], reverse="True")
        
        
        for job in jobs:
            d = job[0]
            p = job[1]
            
            # checking free slot from backward
            for i in range(d, 0, -1):
                if arr[i] == 0:
                    arr[i] = 1
                    count += 1
                    maxProfit += p
                    break
                
        
        return [count, maxProfit]
        
        

# Optimized approach - pq
import heapq
class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        
        maxProfit = 0
        count = 0
        
        # create jobs pair
        jobs = []
        for i in range(len(profit)):
            d = deadline[i]
            p = profit[i]
            
            newJob = (d,p)
            jobs.append(newJob)
            
        jobs.sort() # sort based on deadline in ascending order
        pq = []
        
        for job in jobs:
            d = job[0]
            p = job[1]
            
            if d > len(pq):
                heapq.heappush(pq, p)
            elif pq and p > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, p)
                
        while pq:
            maxProfit += heapq.heappop(pq)
            count += 1
        
        
        return [count, maxProfit]
        
        
        