# Combination Sum

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]


# Approach:
# For each elem we have to options either pick or not pick.
# coz we have infinite supply so we can pick until its valid.
# So applied both and returned final ans






class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(candidates)
        ans = []

        def helper(idx, li,tar):
            if idx == n:
                if tar == 0:
                    ans.append(li[:])
                return
            
            
            # take
            if candidates[idx] <= tar:
                li.append(candidates[idx])
                helper(idx,li,tar-candidates[idx])
                li.pop()

            # not take
            helper(idx+1,li,tar)

        helper(0,[],target)

        return ans
        