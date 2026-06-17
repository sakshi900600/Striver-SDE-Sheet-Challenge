# Combination Sum II

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


# Approach:
# Here we have to eliminate duplicate and also can take each elem once. 
# So to avoid duplicate, I have first sorted the arry.
# Then if valid to take then take it.
# return ans



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        candidates.sort()

        ans = []

        def helper(idx, tar, li):
            if tar == 0:
                ans.append(li[:])
                return
            
            for i in range(idx, n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                
                if candidates[i] > tar:
                    break

                li.append(candidates[i])
                helper(i+1, tar-candidates[i], li)
                li.pop()
        
        
        helper(0,target, [])


        return ans
        