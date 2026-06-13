# 15. 3Sum


# Approach:
# First I sort the arr and then run a loop
# inside this loop: i have written the two sum code
# to avoid duplicates i have checked all pointers from it prev values.
# That's it return ans list

# T.C = nLog(n)
# S.C = O(n)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1
            while l < r:
                csum = nums[i] + nums[l] + nums[r]
                if csum == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l]==nums[l-1]:
                        l += 1
                    while l<r and nums[r]==nums[r+1]:
                        r -= 1
                    
                elif csum < 0:
                    l += 1
                else:
                    r -= 1
        
        return ans
        