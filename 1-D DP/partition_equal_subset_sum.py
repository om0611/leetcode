'''
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two 
subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''

# Key Ideas:
# If it is possible to partition the input array into two subsets with equal sum, each subset must have half the total sum of the array.
# The problem reduces to checking whether it's possible to select a subset of elements that add up to half the total sum.
# We iterate through the array while maintaining a set of all possible partial sums that can be formed so far.
# For each element, we update the set by considering both possibilities: including and excluding the current element.
# If at any point the set contains half the total sum, we return True. 
# We do not need to store sums that are greater than half the total sum in the set.


# Runtime: O(n * (sum(nums) / 2)) because in the worst case, we iterate over all the elments in the input array and our set contains all the 
# numbers between 0 and sum(nums) / 2.


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        totalSum = sum(nums)

        # If the sum of the array is not even, we cannot partition it into two equal sum subsets
        if (totalSum % 2 != 0):
            return False
        
        # Sum of each subset should be half of the total sum if it is possible to create the subsets
        halfSum = totalSum // 2
        sums = {0}

        for i in range(len(nums)):
            newSums = set()
            for t in sums:
                if (t + nums[i] == halfSum):
                    return True
                if (t + nums[i] < halfSum):
                    newSums.add(t + nums[i])
                newSums.add(t)

            sums = newSums
        
        return False