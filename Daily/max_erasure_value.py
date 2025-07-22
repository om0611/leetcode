'''
1695. Maximum Erasure Value

You are given an array of positive integers nums and want to erase a subarray 
containing unique elements. The score you get by erasing the subarray is equal 
to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence
of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
'''


# Key Ideas:
# This is a standard sliding window problem. Maintain a set to store the 
# numbers in the current window. Expand window as long as the new number is not
# already in the set, keeping track of the current window sum alongisde. If
# the new number is in the set, we shrink window from the left until that number
# is no longer in the set, updating the current window sum and the set 
# alongside. We also use a variable to store the maximum sum seen so far, and
# update it during each iteration. Return this variable are iterating through
# the entire list.

# Runtime: O(n) because the right pointer of the window iterates through the
# entire list, and in the worst case, the left pointer also iterates through
# the entire list. The set operations are constant time.

# Space: O(n) because we use a set to store the numbers in the current window, 
# and in the worst case, the set can have as many numbers as the input list. 


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        curr_nums = set()
        curr_sum = 0
        max_sum = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] in curr_nums:
                while nums[l] != nums[r]:
                    curr_sum -= nums[l]
                    curr_nums.remove(nums[l])
                    l += 1

                l += 1
            else:
                curr_sum += nums[r]
                curr_nums.add(nums[r])
                max_sum = max(max_sum, curr_sum)
        
        return max_sum