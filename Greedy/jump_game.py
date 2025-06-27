'''
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length
at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
length is 0, which makes it impossible to reach the last index.
'''


# Key Ideas:
# We will keep track of a number, nextJump, that represents how far the next
# index is from where it is possible to reach the last index. 
# Iterate through nums in reverse order. At the last index, nextJump would be 0.
# At each index i, if the maximum possible jump we can make is greater than
# nextJump, then we can obviously reach the last index from i, so we reset
# nextJump to 0. At the end of each iteration, we increment nextJump. 
# At the end, we return True if nextJump == 0, which means it is possible to 
# reach the last index from the first index.

# Runtime: O(n) because we are iterating through nums and doing constant work
# during each iteration. 

# Space: O(1) because we are only storing a number in memory.


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        nextJump = 0

        for i in range(len(nums) - 2, -1, -1):
            nextJump += 1
            if nums[i] >= nextJump:
                nextJump = 0
        
        return nextJump == 0