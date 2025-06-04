'''
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''

# Key Ideas:
# We can use a 2-D grid to solve this problem. Place word1 along the y-axis
# and word2 along the x-axis. At a cell (i, j), if word1[i] == word2[j], we
# don't need to perform any operations, so we look diagonally to cell 
# (i+1, j+1). If they don't match, we try all three operations. If we want to 
# insert a character at index i in word1, we would obviously want to insert 
# word2[j], which brings us to cell (i, j+1). If we want to replace the current
# character in word1, we would obviously replace it with word2[j], which brings
# us to cell (i+1, j+1). If we delete the current character in word1, we get
# to the cell (i+1, j). Note that each of these operations cost 1. We take the 
# minimum of all three cells + 1. We can build up this grid bottom up. Note 
# that we need an extra row and column in our grid to handle the cases where 
# one or both of the words are empty strings. If both strings are empty, we 
# return 0. 

# Runtime: O(m * n) where m == len(word1) and n == len(word2), and m * n are 
# the dimensions of the grid. This is because we have to calculate the value 
# at each cell in the grid.

# Space: O(n) because we only need to store the current row and the next row in
# memory at a time, and the length of each row is n.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        nextRow = [j for j in range(len(word2), -1, -1)]

        for i in range(len(word1) - 1, -1, -1):
            currRow = [0] * (len(word2) + 1)
            for j in range(len(word2), -1, -1):
                if j == len(word2):
                    # only valid operation is delete
                    currRow[j] = 1 + nextRow[j]

                elif word1[i] == word2[j]:
                    # no operations needed
                    currRow[j] = nextRow[j+1]
                
                else:
                    currRow[j] = 1 + min(
                        currRow[j+1],       # insert the curr char in word2
                        nextRow[j+1],       # replace the curr char in word1 with the curr char in word2
                        nextRow[j]          # delete the curr char in word1
                    )
        
            nextRow = currRow
        
        return nextRow[0]