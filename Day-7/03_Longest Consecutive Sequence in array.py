# Longest Consecutive Sequence


# Approach:
# I have converted the list to set.
# Then I have traversed the set and for each number I checked
# if num-1 not in set then it means we can start a new sequence from here. 
# so i started with cnt=1 and x = that num.
# until x+1 is in set I kept increasing cnt and x.
# and finaly updated longest with max of longest and cnt.
# return longest


# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return 0
        
        s = set(nums)
        longest = 1

        for num in s:
            if num-1 not in s:
                cnt = 1
                x = num

                while x+1 in s:
                    cnt += 1
                    x += 1
                
                longest = max(longest, cnt)
        
        return longest

        
        
