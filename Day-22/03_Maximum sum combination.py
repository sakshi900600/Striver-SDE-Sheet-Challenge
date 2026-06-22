# Maximum sum combination

import heapq
class Solution:
    def topKSumPairs(self, a, b, k):
        # code here
        
        heap = []
        
        for i in range(len(a)):
            for j in range(len(b)):
                csum = a[i] + b[j]
                heapq.heappush(heap, -csum)
        
        cnt = 0
        ans = []
        
        while heap and cnt < k:
            elem = - heapq.heappop(heap)
            ans.append(elem)
            cnt += 1
        
        return ans
        


# optimized approach:
import heapq

class Solution:
    # Function to find k maximum sum combinations
    def topKSumPairs(self, nums1, nums2, k):
        
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        max_heap = [(-(nums1[0] + nums2[0]), 0, 0)]


        visited = set()
        visited.add((0, 0))

        result = []

        for _ in range(k):
            sum_neg, i, j = heapq.heappop(max_heap)

            result.append(-sum_neg)

            # Push next element from nums1 if not visited
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(nums1[i + 1] + nums2[j]), i + 1, j))
                visited.add((i + 1, j))

            # Push next element from nums2 if not visited
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(nums1[i] + nums2[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return result
        
        
