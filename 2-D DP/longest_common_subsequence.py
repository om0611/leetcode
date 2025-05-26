'''
1143. Longest Common Subsequence (LCS)

Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both 
strings.
'''

# Key Ideas:
# If the first characters of text1 and text2 match, then
# LCS(text1, text2) = 1 + LCS(text1[1:], text2[1:]). 
# If the first characters don't match, we get two subproblems
# LCS(text1, text2) = max(LCS(text1, text2[1:]), LCS(text1[1:], text2))
# We can use a grid, with chars of text1 along the left edge and chars of text2 
# along the top edge. At each cell, we compare the corresponding chars. If they
# match, the value of that cell is 1 + the diagonal cell to the bottom right.
# If they don't match, the value of that cell is the max of the cell below and
# the cell to the right. We populate this grid from bottom up.

# Runtime: O(m * n) where m = len(text1) and n = len(text2). The size of the 
# grid is m * n, and we have to calculate the value of each cell. 
# Space: O(n) because we only need to store the current row and the next row, 
# each of which is size n.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)

        nextRow = [0] * (COLS + 1)

        for i in range(ROWS - 1, -1, -1):
            currentRow = [0] * (COLS + 1)
            for j in range(COLS - 1, -1, -1):
                if text1[i] == text2[j]:
                    currentRow[j] = 1 + nextRow[j+1]
                else:
                    currentRow[j] = max(nextRow[j], currentRow[j+1])
            
            nextRow = currentRow
        
        return currentRow[0]