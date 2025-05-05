'''
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean 
touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where 
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, 
and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from 
any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell 
(ri, ci) to both the Pacific and Atlantic oceans.
'''

# Key Ideas:
# Instead of running DFS/BFS on each cell to check if it touches both the Pacific and the Atlantic, we can start
# from the oceans and move inwards to see which cells can be reached. Start at the cells bordering the oceans and
# call DFS, storing visited cells in the respective set (pacific or atlantic). At the end, iterate over each cell
# and check if it is in both pacific and atlantic. If so, add it to the result list.

# Runtime: O(m * n) where m and n are the dimensions of the grid. The DFS traversal visits each cell at most once, 
# and is run twice, once for pacific and once for atlantic. This is O(2 * m * n). At the end, we iterate over each
# cell in the grid, which is O(m * n).


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visit, prev_height):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visit or heights[i][j] < prev_height:
                return

            visit.add((i, j))
            dfs(i-1, j, visit, heights[i][j])
            dfs(i+1, j, visit, heights[i][j])
            dfs(i, j-1, visit, heights[i][j])
            dfs(i, j+1, visit, heights[i][j])


        # Top and bottom edges of the grid
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])
        
        # Left and right edges of the grid
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])

        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        
        return res