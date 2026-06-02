# Sort an array of 0s,1s and 2s
# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


# Logic-1:
# Count no of 0,1 and 2. 
# Then based on count fill the arr with 0,1 and 2.

# Time Complexity: O(n)
# Space Complexity: O(1)


# Logic-2: Dutch National Flag Algorithm:

# The main idea is to 
# Maintain 3 pointers l,m and r. using l pointer move all 0 towards start , using r move all 2 towards end and using m to keep the 1 in middle part of the arr.


# Initalize l,m with 0 and r as n-1
# traverse the arr while m <= r:
# if elem is 0 then move towards start by swapping m,l and moving both forward
# if elem is 1 just move m +1
# if elem is 2 then move towards end by swapping m,r and moving only r backward 

# Why moving l,m both forward when elem is 0 and moving only r when 2 ?
# -> When bringing from the right the incoming element is unexamined, So we can't move m. But when bringing from the left, it's already examined, so we can safely move both pointers.


# Time Complexity: O(n)
# Space Complexity: O(1)



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        c0 = 0
        c1 = 0
        c2 = 0

        for elem in nums:
            if elem ==0:
                c0 += 1
            elif elem == 1:
                c1 += 1
            else:
                c2 += 1
        
        for i in range(c0):
            nums[i] = 0
        for i in range(c0, c0+c1):
            nums[i] = 1
        for i in range(c0+c1, n):
            nums[i] = 2


    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        l = 0
        m = 0
        r = n-1

        while m <= r:
            if nums[m] == 0:
                nums[m],nums[l] = nums[l],nums[m]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m],nums[r] = nums[r],nums[m]
                r -= 1

        
        