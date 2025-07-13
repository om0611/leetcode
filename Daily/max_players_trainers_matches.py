'''
2410. Maximum Matching of Players With Trainers

You are given a 0-indexed integer array players, where players[i] represents 
the ability of the ith player. You are also given a 0-indexed integer array 
trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less 
than or equal to the trainer's training capacity. Additionally, the ith player 
can be matched with at most one trainer, and the jth trainer can be matched 
with at most one player.

Return the maximum number of matchings between players and trainers that 
satisfy these conditions.
'''


# Key Ideas:
# We can be greedy with the solution. Start with the player with the max 
# ability and the trainer with the max capacity. If there is a match, increment
# a counter and move onto the player with the next highest ability and the 
# trainer with the next highest capacity. If its not a match, we move onto the
# next player while keeping the trainer the same. 
# To implement this algorithm, we can first sort players and trainers in 
# reverse order (from highest to lowest). Then, we initialize two pointers, 
# one for the player and the other for the trainers. We use the logic described
# above to increment the pointers and a counter until we reach the end of either
# list.


# Runtime: O(n log(n)) because we are sorting both input lists. Iterating 
# through the lists using pointers is O(n).

# Space: O(1) because we are only storing a counter and two pointers in memory.


class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        count = 0
        p_idx = 0
        t_idx = 0
        while p_idx < len(players) and t_idx < len(trainers):
            if players[p_idx] <= trainers[t_idx]:
                count += 1
                t_idx += 1
            p_idx += 1
        
        return count