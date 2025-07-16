'''
3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.

A subsequence sub of nums with length x is called valid if it satisfies:
(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == 
(sub[x - 2] + sub[x - 1]) % 2.

Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting 
some or no elements without changing the order of the remaining elements.
'''

# Key Ideas:
# First note that there are only two possible remainders when you divide by 2,
# either 0 or 1. For the remainder to be 0, the sum sub[i] + sub[i+1] must be
# even. There are two ways that this can happen: either both numbers are odd
# or both are even. In the definition of a valid subsequence, this would imply 
# that the numbers in the subsequence would have to be all odd or all even. 
# For the remainder to be 1, the sum sub[i] + sub[i+1] must be odd. There is 
# exactly one way that this can happen: one number is odd and the other is even.
# This implies that in the subsequence, the numbers would have alternate in 
# terms of odd and even. 
# 
# We can iterate through nums, applying the 3 cases described above and 
# recording the max length we can get in each case. At the end, we return the
# max length amongst all three cases.


# Runtime: O(n) because we are iterating through nums once and doing constant
# work during each iteration. 

# Space: O(1) because we are only storing a few integer variables in memory. 



class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # Case 1: all odd
        # Case 2: all even
        # Case 3: alternating

        odd_len = 0
        even_len = 0
        alternate_len = 0
        next_even = nums[0] % 2 == 0

        for n in nums:
            if n % 2 == 0:
                even_len += 1
                if next_even:
                    alternate_len += 1
                    next_even = False
            else:
                odd_len += 1
                if not next_even:
                    alternate_len += 1
                    next_even = True
            
        return max(odd_len, even_len, alternate_len)