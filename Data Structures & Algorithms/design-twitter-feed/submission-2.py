class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for f in self.followees[userId]:
            element = self.posts[f][-1] + [f, len(self.posts[f]) - 1]
            heap.append(element)
        if self.posts[userId]:
            element = self.posts[userId][-1] + [userId, len(self.posts[userId]) - 1]
            heap.append(element)
        heapq.heapify(heap)
        res = []
        while len(res) < 10 and heap:
            timestamp, tweetId, userId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                element = self.posts[userId][idx - 1] + [userId, idx - 1]
                heapq.heappush(heap, element)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
