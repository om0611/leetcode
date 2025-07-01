'''
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the
ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station. You begin the journey with
an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction, otherwise
return -1. If there exists a solution, it is guaranteed to be unique.
'''

# Key Ideas:
# Note that if sum(cost) > sum(gas), it is impossible to make the trip without
# running out of gas, so we should return -1. Otherwise, there must be a 
# solution. The problem states that the solution is unique, so there must be 
# exactly one solution. Iterate through the gas and cost lists, keeping track 
# of the gas amount currently in the tank and the index where you started. 
# At each index i, we gain gas[i], so we add it to our total, and we lost 
# cost[i] to get to the next station, so we subtract it from our total. 
# If the total goes below 0, it means we cannot complete the trip from where
# we started, so we move the start position to the next index (i + 1) and reset
# total to 0. The first index that is able to reach to the end of the list is 
# the solution because:
#   1. all indices less than i could not make the trip.
#   2. all indices after i would have a smaller running total than starting
#       starting at index i.


# Runtime: O(n) because we are iterating through the gas and cost lists, and
# doing constant work during each iteration.

# Space: O(1) because we are only storing the total and start position in 
# memory.

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        # a solution exists
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
            
        return start