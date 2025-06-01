'''
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of 
s1 and s2.
'''

# Key Ideas:
# There are two ways to solve this problem: 1. Backtracking with Caching
# 2. DP using a 2-D Grid
# First note that len(s3) must be equal to len(s1) + len(s2) for s3 to be a 
# valid interleaving of s1 and s2, so we can add this check at the start. 
# To solve this problem using the DP method, we place s1 along the y-axis and
# s2 along the x-axis of the grid. Then at each cell, (i, j), the subproblem 
# becomes that can s3[i+j:] be formed by an interleaving of s1[i:] and s2[j:].
# Note that we need an extra row and column to cover the case where either s1
# or s2 is empty but the other string still has characters. We can fill up this 
# grid from the bottom up. Notice that dp[len(s1)][len(s2)] must be True 
# because an empty string can be formed by an interleaving of two empty strings.
# At each cell, if the curr char in s3 matches with the curr char in s1, we
# look down, and if it matches with the curr char in s2, we look to the right.
# If both paths are possible, we explore them both.
# At the end, we return dp[0][0].

# Runtime: O(n * m) where n == len(s1) and m == len(s2), and n * m is the size
# of the grid. This is because we have to calculate each cell in the grid.  

# Space: O(m) because we only need to store the current row and the next row.


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        currRow = [False] * (len(s2) + 1)
        currRow[len(s2)] = True

        # Initialize the last row
        for j in range(len(s2) - 1, -1, -1):
            if s2[j] == s3[len(s1) + j] and currRow[j+1]:
                currRow[j] = True
        
        nextRow = currRow
        for i in range(len(s1) - 1, -1, -1):
            currRow = [False] * (len(s2) + 1)
            for j in range(len(s2), -1, -1):
                if (i < len(s1) and s1[i] == s3[i+j] and nextRow[j]):
                    currRow[j] = True
                if (j < len(s2) and s2[j] == s3[i+j] and currRow[j+1]):
                    currRow[j] = True
        
            nextRow = currRow
        
        return nextRow[0]