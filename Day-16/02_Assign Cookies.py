# Assign Cookies:


# Approach:
# sort both of the array
# traverse while both exists and if condition satisfy then add in maxcnt
# else move pointer accordingly.

# T.C = O(nlogn)
# S.C = O(1)


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        n = len(g)
        m = len(s)
        i = 0
        j = 0
        s.sort()
        g.sort()

        maxcnt = 0
        while i<n and j<m:
            if s[j] >= g[i]:
                maxcnt += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return maxcnt
    