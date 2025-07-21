'''
1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to 
make it fancy.

Return the final string after the deletion. It can be shown that the answer 
will always be unique.
'''

# Key Ideas:
# Initialize an empty list to store the chars of our result string. Use a 
# variable, prev, to store the last char in our result string, and another 
# variable, count, to store the consecutive count of the current char. Iterate 
# over each char in the input string. If the current char is the same as prev 
# and the count is less than 2, we increment count and add the char to the list.
# If the count is equal to 2, addding the current char would make 3 consecutive
# chars, so we don't add it. If the current char is not equal to prev, we 
# update prev to the current char, reset count to 1, and add the char to the 
# list. After iterating through the entire string, we join the list using an 
# empty string and return it. 


# Runtime: O(n) because we iterate through the input string, and during each 
# iteration, we do constant work.

# Space: O(n) because we store the result string in a list. 


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        prev = ""
        count = 0
        for c in s:
            if c == prev:
                if count < 2:
                    count += 1
                    res.append(c)
            else:
                count = 1
                res.append(c)
                prev = c
                
        return "".join(res)