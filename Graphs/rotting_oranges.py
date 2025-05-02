'''
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

# Key Ideas:
# Iterate over each cell in the grid, counting the number of fresh oranges and storing the rotten oranges
# in a queue. Then, run BFS level by level. At the end of each level, increment the time variable and return 
# its value if the number of fresh oranges is 0. If the number of fresh oranges is still greater than 0 by the end 
# of BFS, return -1.

# Runtime: O(m * n) where m and n are the dimensions of the grid. This is because we first iterate through the entire
# grid and then call BFS, which is visits each cell in the grid at most once. 


from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        t = 0
        while q:
            t += 1
            currLen = len(q)
            for _ in range(currLen):
                i, j = q.popleft()

                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    fresh -= 1
                    q.append((i-1, j))
                
                if i < m - 1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    fresh -= 1
                    q.append((i+1, j))
                
                if j > 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    fresh -= 1
                    q.append((i, j-1))
                
                if j < n - 1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    fresh -= 1
                    q.append((i, j+1))
                
            if fresh == 0:
                return t
        
        return -1