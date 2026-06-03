# Merge Intervals
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]


# Approach:
# Sort intervals based on starting time.
# always consider the first interval
# and for rest intervals, check if they are overlapping then update the end time as max of last interval ending, curr interval ending. 
# return the ans list. 


# Time Complexity: O(nlogn) for sorting and O(n) for merging intervals. Overall O(nlogn)
# Space Complexity: O(n) for storing the answer list.



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(intervals)

        intervals.sort()
        ans = []
        ans.append(intervals[0])

        for i in range(1,n):
            last = ans[-1]
            curr = intervals[i]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                ans.append(curr)
        
        return ans

        