'''
1851. Minimum Interval to Include Each Query

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti]
describes the ith interval starting at lefti and ending at righti (inclusive). 
The size of an interval is defined as the number of integers it contains, or 
more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the
size of the smallest interval i such that lefti <= queries[j] <= righti. If no 
such interval exists, the answer is -1.

Return an array containing the answers to the queries.
'''


# Key Ideas:
# Sort the intervals by their start point to process them in order.
# Sort the queries to handle them in ascending order efficiently.
# Use a min-heap to keep track of intervals that could cover the current query.
# The heap stores (interval size, interval end) so we can quickly find the smallest covering interval.
# For each query, add all intervals that start before or at the query point to the heap.
# Remove intervals from the heap that end before the query point since they can't cover the query.
# The top of the heap gives the smallest interval covering the query, or -1 if none exists.
# Store results in a dictionary keyed by query to maintain original query order.
# Finally, build the results list based on the original order of the queries.


# Runtime: O(nlog(n) + mlog(m)) because we are sorting the intervals and the
# queries. At most n push and pop operations in the heap, each costing log(n),
# nlog(n). Iterating through the queries is O(m) and iterating through the 
# intervals is O(n).

# Space: O(m + n) because in the worst case, the heap stores all the intervals,
# which is O(n), and the answers hashmap stores all the queries, which is O(m).

import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        minHeap = []
        answers = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            answers[q] = minHeap[0][0] if minHeap else -1

        res = []
        for q in queries:
            res.append(answers[q])
        return res