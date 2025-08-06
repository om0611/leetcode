'''
1647. Minimum Deletions to Make Character Frequencies Unique

A string s is called good if there are no two different characters in s that 
have the same frequency.

Given a string s, return the minimum number of characters you need to delete 
to make s good.

The frequency of a character in a string is the number of times it appears in 
the string. For example, in the string "aab", the frequency of 'a' is 2, while 
the frequency of 'b' is 1.
'''

# Key Ideas:
# We can use a list where index i stores the number of characters with 
# frequency i. What we want is for each index in this list to have a 
# max value of 1. We iterate through this list, keeping track of the free spots,
# which are indices with value 0. When we encounter an index with value greater
# than 1, we iteratively remove a char from that index and move it to the last 
# free spot until there is only one char at that index. Note that index 0 is a 
# free spot that can be used infinitely many times since index 0 represents a 
# frequency of 0, which is equivalent to deleting all occurences of a char.
# The number of deletions performed for moving a char at index i to the last 
# free spot is equal to the difference between i and the index of the last free
# spot. At the end, we return the total number of deletions.


# Runtime: O(n) because we have to count the frequency of each char in the input
# string, and then iterate through the frequency list, which is of size n. 

# Space: O(n) because we are using a list of size n. 


class Solution:
    def minDeletions(self, s: str) -> int:
        freq_list = [0] * (len(s) + 1)
        freq_dict = {}
        max_freq = 0
        for c in s:
            if c in freq_dict:
                old_freq = freq_dict[c]
                freq_list[old_freq] -= 1
                freq_list[old_freq + 1] += 1
                freq_dict[c] += 1
            else:
                freq_dict[c] = 1
                freq_list[1] += 1

            max_freq = max(max_freq, freq_dict[c])
        
        free_spots = []
        res = 0
        for i in range(max_freq + 1):
            if freq_list[i] == 0:   # no chars with freq i
                free_spots.append(i)
            elif freq_list[i] > 1:  # more than one char with freq i
                while freq_list[i] > 1:
                    if free_spots[-1] == 0:
                        last_free = 0
                    else:
                        last_free = free_spots.pop()
                    res += i - last_free
                    freq_list[i] -= 1
        
        return res

