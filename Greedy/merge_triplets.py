'''
1899. Merge Triplets to Form Target Triplet

A triplet is an array of three integers. You are given a 2D integer array
triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are
also given an integer array target = [x, y, z] that describes the triplet you
want to obtain.

To obtain target, you may apply the following operation on triplets any number
of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to 
become [max(ai, aj), max(bi, bj), max(ci, cj)].

For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], 
triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

Return true if it is possible to obtain the target triplet [x, y, z] as an 
element of triplets, or false otherwise.
'''


# Key Ideas:
# If the value at a particular index in a triplet is larger than the value at 
# that same index in the target, then when we perform the given operation with 
# this triplet, that value will always be in the resulting triplet, which means
# it will never match the target. Therefore, we ignore all such triplets. With 
# the remaining triplets, we get the max value at each index. If that resulting
# triplet matches target, we return True, otherwise False.

# Runtime: O(n) because we have to iterate over each triplet and during 
# each iteration we are doing constant work. 

# Space: O(1) because we are storing the current triplet in memory which is
# an array of 3 elements.


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        curr = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i, v in enumerate(triplet):
                curr[i] = max(curr[i], v)
        
        return curr == target