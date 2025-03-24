'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
'''

# Key Ideas:
# Store the head element of each linked list in a min heap.
# Construct a new linked list by popping from the heap and adding the corresponding element to the list.
# As you pop from the heap, add the next element of the corresponding linked list to the heap.


# Let k == len(lists) and n be the total number of elements across all lists. Then, the runtime is O(n log(k)).


import heapq
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                minHeap.append([lists[i].val, i])
                lists[i] = lists[i].next

        heapq.heapify(minHeap)
        while minHeap:
            val, i = heapq.heappop(minHeap)
            curr.next = ListNode(val=val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(minHeap, [lists[i].val, i])
                lists[i] = lists[i].next
        
        return dummy.next