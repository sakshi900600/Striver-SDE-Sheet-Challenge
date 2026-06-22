# Kth Largest Element in an Array


import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []

        for elem in nums:
            heapq.heappush(heap, -elem)
        
        cnt = 0
        
        while heap:
            elem = heapq.heappop(heap)
            elem = - elem
            cnt += 1

            if cnt == k:
                return elem
        

        return -1
        