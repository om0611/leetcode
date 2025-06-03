'''
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s 
which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3

Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabb_it
ra_bbit
rab_bit
'''

# Key Ideas:
# This problem can easily be solved using a 2-D grid, with s along the y-axis
# and t along te x-axis. At each cell, if the characters of s and t match,
# we explore the diagonal, which represents incrementing the pointers for s
# and t. In either case, we explore the cell below, which represents skipping
# the current character of s. If we reach the end of t, we found one 
# subsequence of s that equals t. We can build up this grid bottom-up.

# Runtime: O(m * n) where m == len(s) and n == len(t). This is because the grid 
# is m * n and we calculate the value of every cell in the grid.

# Space: O(n) because we only need to store the current row and the next row in
# memory at a time.


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        nextRow = [0] * (len(t) + 1)
        nextRow[len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            currRow = [0] * (len(t) + 1)
            currRow[len(t)] = 1

            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    currRow[j] += nextRow[j+1]
                currRow[j] += nextRow[j]
            
            nextRow = currRow
        
        return nextRow[0]