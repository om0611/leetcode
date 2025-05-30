'''
518. Coin Change II

You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount 
of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
'''


# Key Ideas:
# This is an unbounded knapsack problem because each coin can be chosen 
# infinity many times.
# We can use a 2-D grid, with the coins on the x-axis and all numbers from 0
# to amount on the y-axis. At each cell, we either add the current coin to our 
# total, so we look to the right or we skip the coin, so we look down. We add
# the results of both paths. We can fill up this grid from bottom-up. 
# At the end, we return the value of the top-left cell. 

# Runtime: O(m * n) where m == len(coins) and n == amount. This is because we 
# have to calculate the value for each cell of the grid, and the grid is m x n.
# Space: O(n) because we only need to store the current row and the next row in
# memory to calculate the value of the current cell. 


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        nextRow = [0] * (amount + 1)
        nextRow[amount] = 1

        for i in range(len(coins) - 1, -1, -1):
            currRow = [0] * (amount + 1)
            currRow[amount] = 1

            for j in range(amount - 1, -1, -1):
                if coins[i] + j <= amount:
                    currRow[j] += currRow[coins[i] + j]
                currRow[j] += nextRow[j]
            
            nextRow = currRow
        
        return currRow[0]