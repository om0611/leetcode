'''
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing 
path in matrix.

From each cell, you can either move in four directions: left, right, up, or 
down. You may not move diagonally or move outside the boundary 
(i.e., wrap-around is not allowed).
'''

# Key Ideas:
# Brute Force: Run DFS at each cell to find the longest increasing path 
# starting at that cell.
# We can make this efficient by using a cache to store intermediate results. 


# Runtime: O(m * n) where m and n are the dimensions of the matrix. This is 
# because, with the cache, we only visit each cell once during DFS.

# Space: O(m * n) because we are storing the entire grid in memory.


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_so_far = 1
        dp = {}
        visited = set()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = 1
            visited.add((i, j))

            if i > 0 and matrix[i-1][j] > matrix[i][j] and (i-1, j) not in visited:
                dp[(i, j)] = max(dp[(i, j)], 1 + dfs(i-1, j))
            if j > 0 and matrix[i][j-1] > matrix[i][j] and (i, j-1) not in visited:
                dp[(i, j)] = max(dp[(i, j)], 1 + dfs(i, j-1))
            if i < m - 1 and matrix[i+1][j] > matrix[i][j] and (i+1, j) not in visited:
                dp[(i, j)] = max(dp[(i, j)], 1 + dfs(i+1, j))
            if j < n - 1 and matrix[i][j+1] > matrix[i][j] and (i, j+1) not in visited:
                dp[(i, j)] = max(dp[(i, j)], 1 + dfs(i, j+1))

            visited.remove((i, j))
            return dp[(i, j)]
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in dp:
                    max_so_far = max(max_so_far, dfs(i, j))
        
        return max_so_far