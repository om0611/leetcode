'''
Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end 
times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum 
number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.
'''

# Key Ideas:
# The minimum number of days required to schedule all meetings without any 
# conflicts is the maximum number of meetings occuring concurrenty. To
# find this, we iterate over the start and end values in sorted order and keep
# a count variable to store the current number of ongoing meetings. If the 
# current value is a start value, it means a new meeting started, so we 
# increment the counter by 1 and update the max count. If the current value is 
# a end value, it means a meeting ended, so we decrement the counter by 1. 
# To iterate over the start and end values in sorted order, we create two lists,
# one to store the sorted start values and the other to store the sorted end
# values. Then we use two pointers, one for the start values and the other
# for the end values, picking the smaller value at each iteration. 
# At the end, return the max count.


# Runtime: O(nlog(n)) because we need to sort the start and end values. 
# Iterating over the start and end values is O(n) since we are doing constant
# work during each iteration.

# Space: O(n) becuase we are storing the start and end values of each interval.



class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        maxCount = 0
        currCount = 0
        start_pt = 0
        end_pt = 0
        while start_pt < len(intervals):
            if start[start_pt] < end[end_pt]:
                currCount += 1
                start_pt += 1
                maxCount = max(maxCount, currCount)
            else:
                currCount -= 1
                end_pt += 1

        return maxCount