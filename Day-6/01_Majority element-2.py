# Majority element -2


# This problem is similar as the majority elem-1. Here we have to return all elem having freq > n/3.
# Now the point is only 2 elem can have freq > n/3.

# So we can apply the same O(1) sc logic there we were taking only 1 elem here we will take 2 elem and their cnt. 

# rest everything will be same. 

# Time Complexity = O(n)
# Space Complexity = O(1)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # only 2 possible elem can be majority (freq > n/3),so
        n = len(nums)
        cnt1 = 0
        cnt2 = 0
        elem1 = None
        elem2 = None

        for i in range(n):
            if elem1 != None and elem1 == nums[i]:
                cnt1 += 1
            elif elem2 != None and elem2 == nums[i]:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                elem1 = nums[i]
            elif cnt2 == 0:
                cnt2 = 1
                elem2 = nums[i]
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0

        for i in nums:
            if i == elem1:
                cnt1 += 1
            if i == elem2:
                cnt2 += 1

        ans = []
        if cnt1 > n//3:
            ans.append(elem1)
        
        if cnt2 > n//3:
            ans.append(elem2)

        
        return ans
        