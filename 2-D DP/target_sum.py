'''
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' 
and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates 
to target.
'''

# Key Ideas:
# This is a 0/1 Knapsack problem because for each num in nums, you have two
# options: add it (0) or subtract it (1). Since it is a 0/1 Knapsack problem,
# we can try using a 2-D grid. On the y-axis, we have each index in nums. On 
# the x-axis, we have all possible partial sums, from -sum(nums) to +sum(nums).
# At cell dp[i][sum], we store the number of ways to get sum by using nums[:i]
# elements. This means, dp[0][0] = 1 because there is exactly 1 way to get a 
# sum of 0 with 0 elements. Note that we cannot fill up this grid sequentially. 
# Instead, we start at dp[0][0] and then branch down like a tree. At the end,
# we return dp[len(nums)-1][target]. Since not every cell is used, we can use a
# dictionary instead of a list to store each row.

# Runtime: O(n * m) where n == len(nums) and m == sum(nums) because in the 
# worst case, we have to calculate all the cells in the grid, whose dimensions
# are n * m.
# Space: O(m) since we only need to store the current row and the next row, 
# each of which is a dictionary which in the worst case can have m elements.

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        currRow = defaultdict(int)
        currRow[0] = 1      # 1 way to sum up to 0 with no elements

        for i in range(len(nums)):
            nextRow = defaultdict(int)
            for summ, count in currRow.items():
                nextRow[summ + nums[i]] += count
                nextRow[summ - nums[i]] += count

            currRow = nextRow
        
        return currRow[target]