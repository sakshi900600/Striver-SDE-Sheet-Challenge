# Palindrome Partitioning

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]


# Approach:
# Partition on each index and from those if substr is palindrom store in ans
# return ans


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        ans = []

        def helper(idx, li ):
            if idx == n:
                ans.append(li[:])
                return

            for i in range(idx, n):
                if self.ispalindrome(idx,i,s):
                    li.append(s[idx: i+1])
                    helper(i+1, li)
                    li.pop()
        
        helper(0,[])

        return ans
    

    def ispalindrome(self,si, ei, s):
        while si <= ei:
            if s[si] != s[ei]:
                return False
            si += 1
            ei -= 1
        
        return True

        
        