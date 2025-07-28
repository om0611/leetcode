"""
673. Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.


Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and 
[1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there 
are 5 increasing subsequences of length 1, so output 5.
"""


# Key Ideas:
# At each index in the input list, we want to know what is the length of the
# LIS starting at that index and how many subsequences of that length can we 
# create from that index. Initialize two lists, one to store the length of LIS 
# at each index, and the other to store the count of LIS at each index. Iterate
# through the input list in reverse order, and at each index, iterate over 
# all indices that come after it and check:
#   - if 1 + lenLIS[j] > lenLIS[i], we set lenLIS[i] to lenLIS[j] and 
#       count[i] to count[j]
#   - if 1 + lenLIS[j] == lenLIS[i], we add count[j] to count[i]
# 
# After iterating over all indices that come after the current index, we update
# the global variables:
#   - if lenLIS[i] > maxLen, we set maxLen to lenLIS[j] and 
#       res to count[i]
#   - if lenLIS[i] == maxLen, we add count[i] to res
#
# At the end, we return res.


# Runtime: O(n^2) because for each index, we iterate over every index that
# comes after it. The work done during each iteration is constant. 

# Space: O(n) because we are storing two lists of length n. 


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        lenLIS = [1] * len(nums)
        count = [1] * len(nums)
        maxLen = 0
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            currMax = 1
            currCount = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    length = 1 + lenLIS[j]
                    if length > lenLIS[i]:
                        lenLIS[i] = length
                        count[i] = count[j]
                    elif length == lenLIS[i]:
                        count[i] += count[j]
            
            if lenLIS[i] > maxLen:
                maxLen = lenLIS[i]
                res = count[i]
            elif lenLIS[i] == maxLen:
                res += count[i]
        
        return res
