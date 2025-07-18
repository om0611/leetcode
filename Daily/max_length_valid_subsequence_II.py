'''
3202. Find the Maximum Length of Valid Subsequence II

You are given an integer array nums and a positive integer k.

A subsequence sub of nums with length x is called valid if it satisfies:
(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == 
(sub[x - 2] + sub[x - 1]) % k.

Return the length of the longest valid subsequence of nums. 
'''

# Key Ideas:
# Note that (a + b) % k == (a % k) + (b % k). 
# We can simplify the condition for valid subsequence:
# (s[0] + s[1]) % k == (s[1] + sub[2]) % k is equivalent to
# (s[0] % k) + (s[1] % k) == (s[1] % k) + (s[2] % k), which is equivalent to
# (s[0] % k) == (s[2] % k)
# This means that in a valid subsequence, the alternating remainders must be the
# same. 
# We can now solve this using dynamic programming. We can initialize a 2-D 
# grid dp, where dp[r1][r2] represents the length of the longest subsequence
# ending with remainder r2 and the second-last remainder being r1. 
# Iterate through nums and:
#   1. Calculate the modulo k of the current number
#   2. Treat the current remainder as the last remainder of the subsequence. 
#   3. Iterate over all possible remainders that can be in the second-last 
#       position. 
#   4. Update the grid as follows:
#       dp[prev][curr] = dp[curr][prev] + 1
#       because we found the next remainder in the subsequence ending with 
#       (curr, prev).
#   5. Update max length


# Runtime: O(nk) because we iterate through each num in nums and 
# for each number, we iterate through all possible remainders, which is k.

# Space: O(k^2) because we are storing a grid which is k * k.


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        # In a valid subsequence sub, sub[i] % k == sub[i+2] % k == ...
        # and sub[i+1] % k == sub[i+3] % k == ...
        dp = [[0] * k for _ in range(k)]
        res = 0

        for n in nums:
            n %= k
            for prev in range(k):
                dp[prev][n] = dp[n][prev] + 1
                res = max(res, dp[prev][n])

        return res