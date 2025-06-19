'''
Meeting Rooms

Given an array of meeting time interval objects consisting of start and end 
times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a 
person could add all meetings to their schedule without any conflicts.
'''

# Key Ideas:
# Sort the intervals so that we only have to compare consecutive intervals 
# for overlap. To check if two intervals overlap, we compare the end value
# of the previous interval with the start value of the current interval. If the 
# current interval starts before the previous interval has ended, there is an 
# overlap. We iterate through the sorted intervals and check for overlap using 
# the rule described above. If there is an overlap, we return immediately, else
# we return True after iterating over all the intervals.


# Runtime: O(nlog(n)) because we are sorting the input list. Iterating over
# the intervals is O(n) since the work done inside the loop is constant. 

# Space: O(1) because we are only storing the end value of the previous 
# interval, which is a number.


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda i: i.start)
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            if currStart < prevEnd:
                return False
            prevEnd = currEnd
        
        return True
