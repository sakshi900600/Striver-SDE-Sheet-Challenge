# 347. Top K Frequent Elements


# Approach:
# get freq of all elem, stored in heap
# take k elem from heap and return.


import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}
        ans = []

        for elem in nums:
            freq[elem] = freq.get(elem,0)+1
        
        pq = []
        for key,val in freq.items():
            heapq.heappush(pq, (-val,key))
        
        print(pq)
        for _ in range(k):
            val,elem = heapq.heappop(pq)
            ans.append(elem)

        return ans

        