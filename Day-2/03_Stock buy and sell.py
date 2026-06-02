# Best Time to Buy and Sell Stock:
# Input: prices = [7,1,5,3,6,4]
# Output: 5


# Approach: 
# Here we have to buy and sell stock only once. 
# So we have only one option, to buy on day 0. so we will buy
# on next days if prices are less than our assumed buyprice then we will update buyprice
# otherwise we can sell to get profits
# from all possible profits store and return maxpofit.


# Time Complexity: O(n)
# Space Complexity: O(1)



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        buy_price = prices[0]
        max_profit = 0

        for i in range(1,n):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = prices[i] - buy_price
                max_profit = max(max_profit, profit)
        
        return max_profit
    
