# 4 Sum


# Approach:
# I have first sorted the given list. 
# And then extended the 2 Sum approach.
# Here we have to handle duplicates as well, and for that compare elem with prev or next according to pointers and skip duplicates.
# We have to return distinct quadruplets lists so first stored in set and then converted to list.

# Time complexity: O(n^3)
# Space complexity: O(1)


class Solution(object):
    def fourSum(self, nums, tar):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        nums.sort()
        ans = set()

        for i in range(n):
            if i !=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                left = j+1
                right = n-1

                while left < right:
                    csum = nums[i] + nums[j] + nums[left]+nums[right]

                    if csum == tar:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        right -= 1

                        while left < right and nums[left]==nums[left-1]:
                            left += 1
                        
                        while left<right and nums[right]==nums[right+1]:
                            right -= 1
                    elif csum < tar:
                        left += 1
                    else:
                        right -= 1
        
        final_ans = []
        for elem in ans:
            final_ans.append(list(elem))
        
        return final_ans



