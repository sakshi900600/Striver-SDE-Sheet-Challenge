# Kadane's Algo: It is used to find maximum sum of a contiguous subarr in array. It is based on the idea that if sum of subarr is negative then it can never be the maximum sum so instead of continuing with that subarr we can start a new subarr from next elem. 


# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


# Algorithm:
# 1. take maxsum and csum as -inf and 0 respectively.
# 2. traverse the given arr and if csum >= 0 then add elem to csum else assign elem to csum.
# 3. everytime update maxsum with max of maxsum and csum.
# 4. return maxsum at the end.

# Time Complexity: O(n)
# Space Complexity: O(1)



# Approach 2: Divide and Conquer:
# The main idea is we have to find max subarr sum so it will be either in left, right or center part of the array. So for every index calculate all 3 sum and from them whatever will be maximum will be our ans. 

# Important: 
# While calculating center subarr sum, we need to include the mid and then extend sum both left and right side. 
# while calculating left sum make sure to start calculating from mid towards si idx. 


# Time Complexity: O(nlogn)
# Space Complexity: O(log n) recursion


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxsum = float('-inf')
        csum = 0

        for elem in nums:
            if csum >= 0:
                csum += elem
            else:
                csum = elem
            
            maxsum = max(maxsum, csum)
        
        return maxsum
    

    def maxSubArray2(self, nums):
        n = len(nums)

        return self.maxSumDnC(nums, 0, n-1)

    def maxSumDnC(self, nums, si, ei):
        if si == ei:
            return nums[si]

        mid = (si+ei)//2
        left = self.maxSumDnC(nums, si, mid)
        right = self.maxSumDnC(nums, mid+1, ei)
        center = self.maxSumDnC_helper(nums, si, mid, ei)

        return max(left, right, center)


    def maxSumDnC_helper(self, nums, si, mid, ei):
        left_sum = float("-inf")
        right_sum = float("-inf")
        csum = 0

        # maxm sum ending at mid
        for i in range(mid, si-1, -1):
            csum += nums[i]
            left_sum = max(left_sum, csum)
        
        csum = 0

        # maxm sum starting at mid+1
        for i in range(mid+1, ei+1):
            csum += nums[i]
            right_sum = max(right_sum, csum)
        

        return left_sum + right_sum




if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray2(nums))

