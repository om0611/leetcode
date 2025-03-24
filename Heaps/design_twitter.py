'''
355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 
10 most recent tweets in the user's news feed.

Implement the Twitter class:

    Twitter() Initializes your twitter object.

    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this 
    function will be made with a unique tweetId.
    
    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in 
    the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most 
    recent to least recent.
    
    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
    
    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
'''

# Key Ideas
# We can store a mapping between each user and a list of their tweets, where the most recent tweet is at the end of the list.
# We can store a mapping between each user and a set of the people they follow. 
# For getNewsFeed, we store the most recent tweet by the user and by each of the people they follow in a max heap. We then
# pop from the max heap and add the corresponding tweet to the feed. For each popped tweet, we add the next recent tweet
# made by the same user to the heap. 


from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1      # we will use a min heap with negative time values to simulate a max heap

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        maxHeap = []
        self.followers[userId].add(userId)
        for follower in self.followers[userId]:
            if self.tweets[follower]:
                index = len(self.tweets[follower]) - 1
                time, tweet = self.tweets[follower][index]
                maxHeap.append([time, tweet, follower, index - 1])

        heapq.heapify(maxHeap)
        while len(feed) < 10 and maxHeap:
            time, tweet, follower, index = heapq.heappop(maxHeap)
            feed.append(tweet)
            if index >= 0:
                time, tweet = self.tweets[follower][index]
                heapq.heappush(maxHeap, [time, tweet, follower, index - 1])

        self.followers[userId].remove(userId)
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)