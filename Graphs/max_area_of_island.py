'''
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
'''

# Key Ideas:
# Very similar to the problem Number of Islands.
# Iterate over each location in the grid, and at each unexplored land location, call a traversal algorithm, such as dfs.
# Make the algorithm return the area of the island that contains that piece of land. Update the max area.
# Use a set to store the visited locations.

# Runtime: O(m * n) where m is the number of rows in the grid and n is the number of columns. This is because we 
# iterate over each location in the grid exactly once within the loops, and the traversal algorithm
# visits each location at most once. 

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(i, j):
            if (i, j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i, j))
            currArea = 1

            if i > 0:
                currArea += dfs(i-1, j)
            if i < m - 1:
                currArea += dfs(i+1, j)
            if j > 0:
                currArea += dfs(i, j-1)
            if j < n - 1:
                currArea += dfs(i, j+1)

            return currArea
        

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
                
        return maxArea