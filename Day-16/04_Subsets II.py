# Subsets 

# Here we are supposed to generate all subsets.
# I have used take or nottake approach to get all subsets.


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res_set = set()

        def helper(idx, nums,li):
            res_set.add(tuple(li[:]))
            if idx >= len(nums):
                return
            
            # take
            li.append(nums[idx])
            helper(idx+1, nums, li)
            li.pop() #backtrack

            # not take 
            helper(idx+1, nums, li)
        
        li = []
        helper(0,nums,li)
        
        # print(res_set)
        ans = []
        for item in res_set:
            ans.append(list(item))
        
        return ans



nums = [5,2,1]

sol = Solution()
print(sol.subsetsWithDup(nums))