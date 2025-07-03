'''
846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups
so that each group is of size groupSize, and consists of groupSize consecutive
cards.

Given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize, return true if she can rearrange the cards, or false
otherwise.
'''


# Key Ideas:
# Note that if len(hand) is not divisible by groupSize, it is impossible
# to group the cards. Therefore, we can return False early.
# Find the count of each card in the hand. Sort the hand. Iterate through
# each card in the hand, treating it as the first card in a new group. If
# the count of that card is 0, move onto the next card. Once, the first card
# is picked, find the next groupSize - 1 consecutive cards. If any of those 
# consecutive cards have count 0 or they do not appear in the count dictionary,
# return False. If we reach the end successufully, return True.

# Runtime: O(nlog(n)) because we have to sort the input array. 
# Space: O(n) because we have to store the count of each card. 

from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True