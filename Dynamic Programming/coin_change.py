'''
322. Coin Change

You are given an integer array coins representing coins of different values and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination 
of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
'''

# Key Ideas:
# Bottom-up Approach: min number of coins to make up $1, $2, ..., $total. Store the results in an array.
# For each amount, iterate through each coin, subtracting it from the amount and then fetching the stored value for the resulting amount.

# Runtime: O(amount * len(coins))
# Space: O(amount)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(amount+1):
            for c in coins:
                if c <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]