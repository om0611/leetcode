'''
Islands and Treasures (286. Walls and Gates on LeetCode)

You are given a m x n 2D grid initialized with these three possible values:
    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure 
chest than the value should remain INF. Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
'''

# Key Ideas:
# We can run BFS on a treasure to get the shortest distance from each land location to that treasure.
# Since there are multiple treasures, we can run BFS simultaneously on each treasure to avoid
# visiting a land location more than once. To do this, we can initialize the queue with all the treasure
# locations and then run BFS.

# Runtime: O(m * n) where m and n are the dimensions of the input grid. This is because we initially have
# to go through every element in the grid to find all the treasure locations. Then, we run BFS, which 
# visits each element in the grid at most once. 


from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647

        def bfs():
            while q:
                i, j = q.popleft()
                d = grid[i][j] + 1
                if i > 0 and grid[i-1][j] == INF:
                    q.append((i-1, j))
                    grid[i-1][j] = d
                if i < m - 1 and grid[i+1][j] == INF:
                    q.append((i+1, j))
                    grid[i+1][j] = d
                if j > 0 and grid[i][j-1] == INF:
                    q.append((i, j-1))
                    grid[i][j-1] = d
                if j < n - 1 and grid[i][j+1] == INF:
                    q.append((i, j+1))
                    grid[i][j+1] = d

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        bfs()