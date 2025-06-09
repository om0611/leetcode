'''
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with 
a number on it represented by an array nums. You are asked to burst all the 
balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] 
coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if 
there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
'''

# Key Ideas:
# Instead of deciding which balloon to burst first, we can decide which
# balloon to burst last. Suppose we burst the balloon at index i last, then we
# get two subproblems: the left part (from 0 to i-1) and the right part 
# (from i+1 to n-1). More generally, if we an array of balloons from index l to 
# r and we burst the balloon at index i last, then we get two subproblems:
# the left part (from l to i-1) and the right part (from i+1 to r). The coins
# we get from bursting the balloon at index i last is:
# nums[l-1] * nums[i] * nums[r+1]. We can store the results of the subproblems
# in a 2D array dp, where dp[l][r] is the maximum coins we can collect from
# bursting the balloons from index l to r.

# Runtime: O(n^3) because there are O(n^2) subarrays (pairs of l and r) and for 
# each subarray, we iterate through all the balloons in that subarray, which
# is O(n).

# Space: O(n^2) because we are storing the results for all possible subarrays,
# and there are n^2 subarrays.


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            max_coins = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                max_coins = max(max_coins, coins)
            
            dp[(l, r)] = max_coins
            return max_coins
            
        
        nums = [1] + nums + [1]
        return dfs(1, len(nums) - 2)