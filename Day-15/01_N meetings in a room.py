# N meetings in a room



class Solution:
    def maxMeetings(self, start, end):
        
        meetings = [(end[i], start[i], i + 1) for i in range(len(start))]

        meetings.sort()

        result = []
        last_end = -1

        for e, s, idx in meetings:
            if s > last_end:  
                result.append(idx)  
                last_end = e  
        return result

