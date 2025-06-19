'''
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of 
the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For 
example, [1, 2] and [2, 3] are non-overlapping.
'''


# Key Ideas:
# Sorting the intervals would be helpful because you would only need to check
# consecutive intervals for overlap. 
# If two intervals overlap, we would rather keep the interval that ends earlier
# to reduce the chance that it overlaps with any other intervals that come 
# after. Iterate through the intervals, comparing consecutive intervals for 
# overlap and applying the above rule in the case that two intervals overlap. 


# Runtime: O(nlog(n)) because sorting the intervals is O(nlog(n)). Iterating 
# over all the intervals is O(n).

# Space: O(1) because we are only storing the end value of the previous 
# interval in memory, which is just a number.


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < prevEnd:         # overlap
                res += 1
                prevEnd = min(prevEnd, currEnd)
            else:                           # no overlap
                prevEnd = currEnd
            
        return res