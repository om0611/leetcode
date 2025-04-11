'''
213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were 
broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
'''

# Key Ideas:
# Notice that we have two choices, start from the first house but exclude the last house, or start from the second house 
# including the last house but excluding the first house. These are two subproblems that can be solved using the same algorithm
# as used in House Robber I. At the end, we want to return the max of these two subproblems.

# Runtime: O(n) because we are iterating through the array twice and doing constant work for each iteration.
# Space: O(1) because we are passing in indices into the helper instead of creating new lists using list slicing.


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        

        def helper(start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end):
                prev1, prev2 = max(prev2 + nums[i], prev1), prev1
            return prev1
        
        
        # Rob the first house and not the last house
        rob1 = helper(0, len(nums) - 1)
        # Rob the last house and not the first
        rob2 = helper(1, len(nums))

        return max(rob1, rob2)