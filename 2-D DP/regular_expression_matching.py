'''
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching 
with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

# Key Ideas:
# We should first group all stars (*) with their preceding characters in p.
# Now, we use a 2-D grid, with s along with x-axis and p along the y-axis. 
# When we are at a cell where the current char in p is grouped with a star, 
# we can choose to have 0 of that char, which means looking down a cell since
# we have incremented the pointer for p but not for s. 
# However, if the char matches the current char in s, we can also choose
# to have an instance of that char, which means looking to the right since we 
# have incremented the pointer for s but not for p. 
# When the current char in p is a dot (.) or if it matches the current char in
# s, we look at the bottom-right diagonal cell since we have incremented the
# pointer for both s and p. We can build this grid from the bottom up.


# Runtime: O(n * m) where n == len(s) and m == len(p), and n * m are the 
# dimensions of the grid. This is because we have to calculate the value at
# each cell in the grid, and calculating the value at a cell is constant time
# operation since the cells it looks at have already been computed. 

# Space: O(n) because we only need to store the current row and the next row in
# memory at a time, and the length of a row is n. 


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = []
        for c in p:
            if c == '*':
                pattern[-1] += c
            else:
                pattern.append(c)
        print(pattern)

        nextRow = [False] * (len(s) + 1)
        nextRow[len(s)] = True

        for i in range(len(pattern) - 1, -1, -1):
            currRow = [False] * (len(s) + 1)
            currRow[len(s)] = (pattern[i][-1] == '*' and nextRow[len(s)])

            for j in range(len(s) - 1, -1, -1):
                if pattern[i][-1] == '*':
                    c = pattern[i][0]
                    currRow[j] = nextRow[j]
                    if (c == "." or c == s[j]) and currRow[j+1]:
                        currRow[j] = True  

                elif pattern[i] == '.' or pattern[i] == s[j]:
                    currRow[j] = nextRow[j+1]
            
            nextRow = currRow
        
        return nextRow[0]