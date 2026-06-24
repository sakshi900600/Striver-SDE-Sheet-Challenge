# Word Break


# Approach:
# Using recursion check if word exists in dct or not by getting all substrings.
# If exists then search for next words in dct and if all found and reached at last idx then return true
# otherwise return false

# Although it gives TLE, coz here we are trying all substrings


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        word_set = set(wordDict)

        def helper(idx):
            # If we've reached the end of the string, we've successfully segmented it
            if idx == n:
                return True
                
            for j in range(idx, n):
                substr = s[idx:j+1]
                
                if substr in word_set:
                    # If we've matched a word that reaches the end, return True
                    if j == n - 1:
                        return True
                    
                    # Continue from j+1 (after the matched word)
                    if helper(j+1):
                        return True
            
            return False
        
        return helper(0)
    

# Optimized solution:
# dp[i] = True if the substring s[0:i] (the first i characters of s) can be segmented into words from the dictionary.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always segmentable
        
        for i in range(n):
            if dp[i]:
                for j in range(i+1, n+1):
                    if s[i:j] in word_set:
                        dp[j] = True
        
        return dp[n]
    
    