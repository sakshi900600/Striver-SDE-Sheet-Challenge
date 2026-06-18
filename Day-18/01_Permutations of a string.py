# Permutations

# In this problem we have to generate all permutations

# I have used recursive approach
# We have total n positions to fill and for each position we have some options
# So checking for all valid options and filling 
# when got all pos filled stored that solution
# return final ans solution



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        isused = [0]*n

        def helper(idx, li,isused):
            if idx == n:
                ans.append(li[:])
                return
            
            for i in range(n):
                if isused[i] == 0:
                    isused[i] = 1
                    li.append(nums[i])
                    helper(idx+1, li, isused)
                    li.pop()
                    isused[i] = 0

        helper(0, [], isused)

        return ans 
        