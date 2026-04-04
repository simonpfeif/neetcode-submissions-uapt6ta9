class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

        # hash of userids to followeeID
        # hash of userids to (time, tweetID)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # populate minHeap with first k number of users with list of tweets
        self.followMap[userId].add(userId) # add the users own tweets to feed
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
