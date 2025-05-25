'''
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

# Key Ideas:
# Break the problem into subproblems: what is the min cost to get to the ith step?
# minCost(i) = min(minCost(i-1), minCost(i-2)) + cost[i]
# We only need to store the previous two results.


# Runtime: O(n) because the for loop iterates n times and everything else is constant.
# Space: O(1) since we are only storing the previous two results, which is constant space.

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev1, prev2 = cost[1], cost[0]
        for i in range(2, len(cost)):
            prev1, prev2 = min(prev1, prev2) + cost[i], prev1

        return min(prev1, prev2)