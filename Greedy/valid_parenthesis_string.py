'''
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', 
return true if s is valid.

The following rules define a valid string:
    - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    - Any right parenthesis ')' must have a corresponding left parenthesis '('.
    - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    - '*' could be treated as a single right parenthesis ')' or a single left 
        parenthesis '(' or an empty string "".
'''


# Key Ideas:
# At the wildcard ('*'), we can choose to make it a close parenthesis, which 
# would decrement our open parenthesis count by 1, or we can make it an open
# parenthesis, which would increment our open parenthesis count by 1. We can
# keep track of the minimum and maximum open parenthesis count as we iterate
# through the string. If the maximum open count goes below 0, it means that the
# open parenthesis are less than close parenthesis and we cannot recover from
# it, so we should return False. Whenever the minimum open count goes below 0, 
# but the maximum open count is >= 0, we do have a choice to prevent the open
# parenthesis from being less than the close parenthesis, so we should reset 
# the min count to 0. Note that at an open parenthesis, both counts are 
# incremented by 1, and at a close parenthesis, both counts are decremented by
# 1. At the end, we return if the min count is equal to 0. 

# Runtime: O(n) because we are iterating through the string once and doing 
# constant work during each iteration. 

# Space: O(1) because we are storing two integers in memory, the min count and 
# the max count.


class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax = 0, 0
        for c in s:
            if c == "(":
                openMin += 1
                openMax += 1
            elif c == ")":
                openMin -= 1
                openMax -= 1
            else:
                openMin -= 1
                openMax += 1
            
            if openMax < 0:
                return False
            if openMin < 0:     # and openMax >= 0
                openMin = 0

        return openMin == 0