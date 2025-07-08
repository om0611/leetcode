'''
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as
possible so that each letter appears in at most one part. For example, the
string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as
["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in
order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''

# Key Ideas:
# We will use a list to store the start and end indices for each partition. 
# We will also use a hashmap to map each character to the first index it is 
# seen in the string. We iterate over each character in the string, and if the
# character is in the hashmap, we get its index from the hashmap and repeatedly
# pop partitions from the list until we get to the partition containing that 
# index. Then we change the end value of that interval to be the current index.
# In the end, we iterate through the partitions, calculating the length of each
# partition and adding it to the output list.

# Runtime: O(n) because we iterate through the string and over all the 
# iterations, we would pop at most n partitions. At the end, we iterate over 
# all the partitions, and there can be at most n partitions. 

# Space: O(n) because we are storing the partitions, and there can be at most
# n partitions. Storing the characters in the hashmap is O(26) = O(1) because
# there are only 26 lowercase characters.


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        parts = []
        visited = {}
        for i in range(len(s)):
            char = s[i]
            if char in visited:
                index = visited[char]
                start, end = parts.pop()
                while start > index:
                    start, end = parts.pop()
                parts.append([start, i])
            else:
                parts.append([i, i])
                visited[char] = i
        
        return [end-start+1 for start, end in parts]