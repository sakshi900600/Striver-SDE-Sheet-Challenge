# Remove duplicate from sorted array

# Input: nums = [1,1,2]
# Output: 2

# Approach:
# Take a pointer at start
# iterate given arr and if curr value is not same as value at pointer idx then put the curr value at pointer idx.
# at the end return pointer +1 idx.

# T.C = O(n)
# S.C = O(1)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        i = 0
        for j in range(1,n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i+1
        
        
        