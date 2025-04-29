'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

# Key Ideas:
# Iterate over each element in the matrix and at each element, if it is land, call a traversal algorithm, such as dfs or bfs, on it. 
# During the traversal, add the location (i, j) to a visited set and explore its neighbours (top, right, bottom, left).
# Once the traversal is complete, increment the counter for the number of islands.

# Runtime: O(m * n) where m is the number of rows in the grid and n is the number of columns. This is because we 
# iterate over each location in the grid exactly once within the loops, and the traversal algorithm
# visits each location at most once. 

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(i, j):
            if grid[i][j] == "0" or (i, j) in visited:
                return

            visited.add((i, j))
            
            if i > 0:
                dfs(i-1, j)
            if j > 0:
                dfs(i, j-1)
            if i < m - 1:
                dfs(i+1, j)
            if j < n - 1:
                dfs(i, j+1)

            return


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    res += 1

        return res