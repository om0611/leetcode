'''
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform 
this operation at most k times.

Return the length of the longest substring containing the same letter you can 
get after performing the above operations.
'''

# Key Ideas:
# We intialize an empty window with two pointers. We also keep track of the char
# count of the current window using a dict. We expand the window to the right,
# updating the char count with the new char. If the length of the current window
# minus the frequency of the most frequent char in our window is less than or
# equal to k, it means that we can replace all other chars to the most freq
# char, so we can continue expanding our window. However, if the value is 
# greater than k, we need to shrink the window from the left. We keep track of 
# the max length using a variable and update it each time we expand the window.


# Runtime: O(n) because the right endpoint of our window goes through every
# index in the input string. In the worst case, our left endpoint also goes
# through every index in the input string, which means we iterate through the
# string twice, making the runtime O(2n) = O(n).


# Space: O(1) because the char count dict can have a max length of 26 because
# the input string only contains uppercase English characters. We are storing
# left and right endpoints of the current window and the max length, which are
# all numbers. 


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # [l, r] represents the current substring
        maxLength = 0
        charCount = defaultdict(int)
        l = 0
        for r in range(len(s)):
            charCount[s[r]] += 1
            maxFreq = max(charCount.values())

            while (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1
                maxFreq = max(charCount.values())

            maxLength = max(maxLength, r - l + 1)
        
        return maxLength