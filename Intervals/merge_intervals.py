'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# Key Ideas:
# Drawing the intervals on a number line helps to visualize the problem.
# Notice that sorting the intervals (by their start value) would be helpful. 
# Once sorted, we iterate over all the intervals, checking if the current
# interval overlaps with the previous interval. If the previous interval's 
# end value is greater than or equal to the current interval's start value, 
# then they are overlapping. If they are overlapping, we merge them by setting
# the end value of the previous interval to be the max of itself and the end
# value of the current interval. If they are not overlapping, we add the
# previous interval to the result list.


# Runtime: O(nlog(n)) because sorting is nlog(n). Iterating over the intervals
# is n. 

# Space: O(1) extra space but O(n) with the return list.


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(prev)
                prev = intervals[i]

        res.append(prev)
        return res