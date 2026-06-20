# 540. Single Element in a Sorted Array


# Approach-1:
# Take xor as 0 and xor all elem of given arr
# at the end whatever will be stored in xor will be that single number.
# 0 ^ a = a , a^a = 0



class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for elem in nums:
            xor = xor ^ elem
        
        return xor
    

