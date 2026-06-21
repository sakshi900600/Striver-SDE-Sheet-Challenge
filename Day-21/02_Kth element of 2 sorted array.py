# Kth element of 2 sorted array


# Here i have used heap, coz that is very simple and straight forward solution


import heapq
class Solution:
    def kthElement(self, a, b, k):
        # code here
        
        heap = []
        
        for elem in a:
            heapq.heappush(heap, elem)
        
        for elem in b:
            heapq.heappush(heap, elem)
        
        
        cnt = 0
        while heap:
            val = heapq.heappop(heap)
            cnt += 1
            
            if cnt == k:
                break
        
        
        return val
            
        
