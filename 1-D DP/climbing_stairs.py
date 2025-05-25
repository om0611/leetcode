'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# Key Ideas:
# Break the problem into subproblems: how many ways to climb to the 1st step, 2nd, 3rd ...
# Number of ways to climb to step i = Number of ways to climb to step (i-1) + Number of ways to climb to step (i-2)
# We don't need to store all the results. We only need the results of the last two steps. 

# Runtime: O(n) because the for loop iterates n times and everything else is constant. 
# Space: O(1) because we are only storing the last two results, which is constant space.


class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 0
        for i in range(1, n+1):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1