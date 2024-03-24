class Twitter:

    def __init__(self):
        self.counter = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.counter,tweetId])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                counter, tweetId = self.tweetMap[followeeId][-1]
                heapq.heappush(minHeap,[counter,tweetId, followeeId, index - 1])
        
        while minHeap and len(ans)<10:
            counter,tweetId, followeeId, index = heapq.heappop(minHeap)
            ans.append(tweetId)
            if index >= 0:
                counter, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[counter,tweetId, followeeId, index - 1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)