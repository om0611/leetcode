'''
91. Decode Ways

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes 
are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

# Key Ideas:
# Two cases: 1. consider the curr char seperately and recurse on the rest of the string. 2. consider the curr char with the next char and recruse on the rest of the string.
# Use memoization to avoid repeated work. 


# Runtime: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def helper(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                dp[i] = 0
                return dp[i]

            if i == len(s) - 1:
                dp[i] = 1
                return dp[i]

            dp[i] = helper(i+1)     # case: consider curr char seperately

            if (s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += helper(i+2)    # case 2: consider curr char with next char

            return dp[i]
        
        return helper(0)