# 295. Find Median from Data Stream


# Approach:
# Take a list and add elem in this lis
# get the mid for even and odd for  both form this list
# it get submited. 


class MedianFinder(object):

    def __init__(self):
        self.li = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.li.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.li)
        self.li.sort()

        if n % 2 == 1:
            return self.li[n//2]

        e1 = self.li[n//2]
        e2 = self.li[n//2 - 1]

        return (e1+e2)/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()