'''
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence 
of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

# Key Ideas
# Bottom-up DP: Start from the end of the string, and at each character, check if we can fit any of the words in wordDict starting
# at this index. If we can, check if the next index after fitting in the word is True in the dp array. If so, set dp[current index] = True.
# At the end, return the value of dp[0]. 

# Runtime: O(n * m * t) where n is the length of the input string s, m is the number of words in wordDict, and t is the max length of a word
# in wordDict. This is because we iterate through each character in the input string, which is O(n). For each character, we iterate over
# all the words in wordDict in the worst case, which is O(m). For each word, we compare it with the string starting at the current index,
# which is O(t).


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if len(w) <= len(s) - i:
                    dp[i] = (w == s[i: i+len(w)] and dp[i+len(w)])
                    if dp[i]:
                        break
            
        return dp[0]
