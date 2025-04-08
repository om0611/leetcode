'''
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

# Key Ideas:
# Iterate over the elements in the input array and at each element, keep track of the max product and min product of a subarray 
# ending at that element. Use the max product to update the result variable at each iteration.
# Handle the edge case where the element is 0.

# Runtime: O(n)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                res = max(res, n)
            else:
                temp = currMax
                currMax = max(currMax * n, currMin * n, n)
                currMin = min(temp * n, currMin * n, n)
                res = max(res, currMax)
        
        return res