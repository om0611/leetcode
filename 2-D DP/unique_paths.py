'''
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right 
at any point in time.

Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.
'''

# Key Ideas:
# This problem is like calculating the Pascal's triangle values. 
# The top edge and the left edge of the grid are all 1s. 
# grid[i][j] = grid[i-1][j] + grid[i][j-1]
# However, we don't need to create the entire grid. We only need to keep
# track of the current row and the previous row, which is a space optimization.

# Runtime: O(m * n) because we create a new array of size n for each row.
# Space: O(n) because we are only storing the current row and the previous row,
# which are both arrays of size n.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_row = [1] * n
        current_row = [0] * n
        current_row[0] = 1

        for _ in range(1, m):
            for j in range(1, n):
                current_row[j] = current_row[j-1] + last_row[j]

            last_row = current_row
            current_row = [0] * n
            current_row[0] = 1
        
        return last_row[n-1]