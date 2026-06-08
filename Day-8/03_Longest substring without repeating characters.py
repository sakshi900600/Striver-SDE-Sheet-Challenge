# 3. Longest Substring Without Repeating Characters


# Input: s = "abcabcbb"
# Output: 3


# Approach:
# I have used sliding window technique.
# take a set to store unique chars
# traversed and until curr char exists in set shrink the wndo by removing ith char from set.
# add the curr char in set
# store the maxlen everytime.
# return maxlen


# Time Complexity: O(n)
# Space Complexity: O(n)



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        str_set = set()
        longest = 0

        i = 0
        for j in range(n):
            ch = s[j]

            while ch in str_set:
                str_set.remove(s[i])
                i += 1
            
            str_set.add(s[j])
            longest = max(longest, j-i+1)

        return longest
        
