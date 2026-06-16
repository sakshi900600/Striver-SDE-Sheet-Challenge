# Minimum Coins



class Solution(object):
    def coinChange(self, coins, amount):
        
        dp = [float("inf")]*(amount+1)

        # dp[i] = min coins needed to make amount i
        dp[0] = 0 # 0 coins needed for amount 0

        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        
        if dp[amount] == float('inf'):
            return -1
            
        return dp[amount]
        