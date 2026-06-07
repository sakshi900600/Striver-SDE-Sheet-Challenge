# Two Sum


# Approach:
# I have taken a dict and stored value,idx of an element while traversing list. 
# so everytime checking req as target-curr elem, and if that already exists in dct then we have found the pair so return the idx of req and curr elem.


# Time complexity: O(n)
# Space complexity: O(n)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        
        n = len(nums)
        dct = {}

        for i in range(n):
            req = target - nums[i]
            if req in dct:
                return [dct[req], i]
            
            dct[nums[i]] = i

        
        return -1
            
