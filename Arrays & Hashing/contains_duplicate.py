'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in 
the array, and return false if every element is distinct.
'''

# Key Ideas:
# Initialize an empty set. As you iterate over the input list, if the current
# number already exists in the set, immediately return True. Otherwise, add the 
# number to the set and continue to the next number.
# If the loop exits without early return, return False because we did not find
# a duplicate.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False