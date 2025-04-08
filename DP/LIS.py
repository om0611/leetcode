'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

# Key Ideas
# Bottom-up DP: Iterate through nums in reverse order, and at each index, store the length of the longest increasing 
# subsequence starting at that index in a dp array. To calculate the LIS at index i, you have to iterate over all the 
# elements after index i and take the max of the LIS starting at each index but only if the element at that index is 
# greater than nums[i]. At the end, return the max of the dp array. 

# Runtime: O(n^2) because at each index, you are checking all the elements after that index. 

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = 1
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            
            res = max(res, dp[i])
        
        return res