# Find duplicate number without modifying the array and using only constant extra space

# Input: nums = [1,3,4,2,2]
# Output: 2


# Approach:
# 1. We can use 2 loops to find duplicate
# 2. we can sort the array and find duplicate
# 3. we can use list or set and append given arr elem if already exist then thats duplicate
# 4. we can use dict to count elem freq and return duplicate

# All these solutions is correct but we are either modifying array or using extra space. 


# Let's optimize it.
# We use the similar code as we use in cycle detection in linkedlist. 



class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        s = set()

        for i in range(n):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return nums[i]
        
        return -1
    

    def findDuplicate_opt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
                

        