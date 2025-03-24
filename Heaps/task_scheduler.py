'''
621. Task Scheduler

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in 
any order, but there's a constraint: there has to be a gap of at least n intervals between 
two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
'''

# Key Ideas:
# At each iteration, we should add the most frequent task. We could use a max heap for this.
# We need to store the tasks that are on cooldown. We could use a queue for this.
# We need to keep track of time.

from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-count[task] for task in count]      # to store the tasks by frequency
        heapq.heapify(maxHeap)

        q = deque()         # to store the tasks currently on cooldown
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)     # we add 1 since we are storing negative values
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
    
        return time