'''
130. Surrounded Regions

Given an m x n matrix board containing letters 'X' and 'O', capture the regions that are surrounded:

Connect:  A cell is connected to adjacent cells horizontally or vertically.
Region:   To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and 
          none of the region cells are on the edge of the board.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
You do not need to return anything.
'''

# Key Ideas:
# Iterating through every O cell and checking if it is surrounded is complicated. Instead, notice
# that an O cell is not surrounded if it is connected to the edge of the board. So, we can call 
# DFS on all O cells that are on the edge of the board and store all the O cells we can reach within 
# a set. At the end, all the O cells that are not in this set are surrounded, so we can replace them with X.

# Runtime: O(n * m) where m and n are the dimensions of the board. DFS visits each cell at most 
# once, so it is O(n * m). At the end, we iterate over the entire board, which is O(n * m).

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] == "X":
                return
            
            visited.add((i, j))

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)


        # Top edge and bottom edge
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)

        # Left edge and right edge
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
