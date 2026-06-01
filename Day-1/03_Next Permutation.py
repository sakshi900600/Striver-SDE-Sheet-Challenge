# Next Permutation:
# Input: nums = [1,2,3]
# Output: [1,3,2]


# Logic:
# This problem is all about observations. 

# To find out permutations, we have some digits fixed and we rearrange the rest digits and when all possible rearrangement are done then we fix some more digits.
# Ex- [1,2,3,4],  first 1 is fixed so rearrangements = [1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2]


# To get the next permutation we need to find out that transition point from where the digit will be rearranged. and we can find that by finding an elem from end of the arr where sorting condn is breaked. 

# after that we will find out just greater elem from it and swap it with that elem.

# then reverse the suffix part.

# time complexity: O(n)
# space complexity: O(1)



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i],nums[j] = nums[j],nums[i]
        
        start = i+1
        end = n-1

        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        return nums

      
