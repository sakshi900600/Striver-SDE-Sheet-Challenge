# Maximum Consecutive Ones

# Input: nums = [1,1,0,1,1,1]
# Output: 3

# Approach:
# Traversed arr, cnt ones
# If got 0 then stored max ones cnt and put cnt = 0 
# at the end storing max ones cnt
# return maxcnt

# T.C = O(n)
# S.C = O(1)



class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        cnt = 0
        maxcnt = 0

        for i in range(n):
            if nums[i] == 1:
                cnt += 1
            else:
                maxcnt = max(maxcnt, cnt)
                cnt = 0
        
        maxcnt = max(maxcnt, cnt)

        return maxcnt

        