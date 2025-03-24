'''
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
    
    MedianFinder() initializes the MedianFinder object.
    
    void addNum(int num) adds the integer num from the data stream to the data structure.
    
    double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.
'''

# Key Ideas:
# Use a max heap to store the smaller half of the elements, and use a min heap to store the greater half of the elements.
# Now, you have access to the middle values: the max element in the max heap and the min element in the min heap.


import heapq

class MedianFinder:

    def __init__(self):     # O(1)
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:     # O(log(n))
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) - len(self.minHeap) == 2:
                num = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, num)

        else:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) - len(self.maxHeap) == 2:
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -num)


    def findMedian(self) -> float:      # O(1)
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]        
