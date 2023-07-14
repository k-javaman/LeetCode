class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users=collections.defaultdict(list)
        self.time=1
        self.followers=collections.defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.users[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news=list(self.users[userId])
        for user in self.followers[userId]:
            news.extend(self.users[user])
        news.sort(reverse=True,key=lambda x:x[0])
        res=[]
        for i in range(len(news)):
            if i == 10: break
            res.append(news[i][1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)