'''
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially
positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index
i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are 
generated such that you can reach nums[n - 1].
'''

# Key Ideas:
# A BFS solution. We maintain a current interval using two pointers. Initially,
# the interval will contain only the first element. We iterate over each 
# element in the current interval to find the maximum index we can reach. 
# Then, our new interval becomes [l', r'] where l' = r + 1 and r' = maxJump. 
# The number of different intervals we have to explore gives us the minimum
# number of jumps to reach the last index. We stop when the current interval
# includes the last index (r >= len(nums) - 1). 

# Runtime: O(n) because we iterate over each element in the input array at most
# once. 

# Space: O(1) because we are only storing the pointers in memory. 


class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        
        return res