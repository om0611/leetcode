'''
57. Insert Interval

You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the ith 
interval and intervals is sorted in ascending order by starti. You are also 
given an interval newInterval = [start, end] that represents the start and end 
of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array 
and return it.
'''


# Key Ideas:
# Iterate through the intervals and compare the current interval with the new
# interval. If the new interval comes completely before the current interval,
# add it to the result list, add the remaining intervals to the list, and 
# return the list. If the current interval comes completely before the new 
# interval, add the current interval to the result list and continue to the 
# next interval. Otherwise, the new interval overlaps with the current interval.
# In this case, merge the two intervals as follows:
# start, end = [min(start, curr_start), max(end, curr_end)]
# We shouldn't add the interval to the result list yet because it may overlap
# with the later intervals. After iterating through all the intervals,
# add the new interval to the result list and return the list.


# Runtime: O(n) where n == len(intervals) because we have to iterate through
# all the intervals. The work done within the loop body is constant.

# Space: O(1) extra space but O(n) with the return list.


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        start, end = newInterval
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            # Case 1: new interval comes completely before the current interval
            if end < curr_start:
                res.append([start, end])
                return res + intervals[i:]
            # Case 2: new interval comes completely after the current interval
            elif curr_end < start:
                res.append([curr_start, curr_end])
            # Case 3: new interval overlaps with the current interval
            else:
                start, end = min(start, curr_start), max(end, curr_end)
        
        res.append([start, end])
        return res