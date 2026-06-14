# Trapping Rain Water

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Approach:
# In order to get total trapped water.
# I find out left and right boundary for each heights
# Then water level will be minimum of both left and right boundary
# To get the actual trapped water we need to substract height from water level.
# Did that and added total trapped water into a variable
# returned total value.


# T.C = O(n)
# S.C = O(n) 



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        left_bound = [0]*n
        left_bound[0] = height[0]

        for i in range(1, n):
            left_bound[i] = max(left_bound[i-1], height[i])

        right_bound = [0]*n
        right_bound[n-1] = height[n-1]

        for i in range(n-2,-1,-1):
            right_bound[i] = max(right_bound[i+1], height[i])
        

        water_level = [0]*n
        trapped_water = 0

        for i in range(n):
            water_level[i] = min(left_bound[i], right_bound[i])
            trapped_water += water_level[i] - height[i]
        
        return trapped_water
        