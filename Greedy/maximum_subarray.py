'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and 
return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

# Key Ideas:
# Initialize two variables, one to store the max subarray sum seen so far and
# the other to store the current sum. Iterate through nums. At the start of 
# each iteration, if the current sum is less than 0, we make it 0 since 
# it is not contributing anything. Add the current number to the current sum. 
# Update max sum with the max of itself and the current sum.
# This is known as the Kadane's Algorithm.

# Runtime: O(n) because we are iterating through the input array but the
# work done during each iteration is constant. 

# Space: O(1) because we are only storing two numbers in memory, maxSum and 
# currSum.


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)
        
        return maxSum