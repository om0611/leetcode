'''
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times) with 
the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown 
one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).
'''


# Key Ideas:
# On each day, you have two decisions: either Buy/Sell or Cooldown. 
# If you buy on ith day: profit = dfs(i+1, 'S') - prices[i].
# If you sell on ith day: profit = dfs(i+2, 'B') + prices[i].
# If you cooldown on ith day: profit = dfs(i+1, buy_or_sell).
# We can store results in a cache to avoid repeated work.

# Runtime: O(2n) because each index in prices is processed at most twice, once 
# when buying and once when selling. The result is stored in the cache to
# avoid repeated work. 

# Space: O(2n) because we store each index in prices twice, once when buying 
# and once when selling.  


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        df = {}

        def dfs(i, buy_or_sell):
            if i >= len(prices):
                return 0
            if (i, buy_or_sell) in df:
                return df[(i, buy_or_sell)]

            if buy_or_sell == 'B':
                df[(i, buy_or_sell)] = max(dfs(i+1, 'S') - prices[i], dfs(i+1, 'B'))
            else:
                df[(i, buy_or_sell)] = max(dfs(i+2, 'B') + prices[i], dfs(i+1, 'S'))
                
            return df[(i, buy_or_sell)]

        return dfs(0, 'B')