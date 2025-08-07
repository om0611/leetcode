'''
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good 
subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that 
x = n * k. 0 is always a multiple of k.
'''

# Key Ideas:
# We can compute prefix sums and store their remainder when divided by k. If
# the remainders at indices i and j (i < j) are the same, it means that we added
# a multiple of k to the prefix sum at index i. Therefore, we return True if the
# length of the subarray (j - i) is at least two. We can use a hashmap to store
# the remainders, mapped to their corresponing index. 
# There is an edge case where if the solution is a subarray that includes the
# first element, our solution would not recognize it as a solution since 0 is
# not already stored in our hashmap. For example, if nums = [1, 2, 3] and k = 6,
# our prefix sums would be [1, 3, 6] and our hashmap would look like: 
# {1: 0, 3: 1, 0: 2} but we wouldn't return True since no remainder was 
# repeated. To handle this edge case, we need to add (0, -1) to our hashmap.
# Alternatively, we could handle this case by returning True when we see a
# remainder of 0. 


# Runtime: O(n) since we are doing only one pass through the array. 

# Space: O(k) since there are k possible remainders when dividing by k.


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainders = {0: -1}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            r = curr_sum % k
            if r not in remainders:
                remainders[r] = i
            elif i - remainders[r] > 1:
                return True

        return False