import collections
# https://leetcode.com/problems/design-twitter/submissions/915263986/

class Twitter:
    def __init__(self):
        self.count = 0
        self.follows = collections.defaultdict(list)
        self.tweets = collections.defaultdict(list)
        self.time = collections.defaultdict(int)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append(tweetId)
        self.time[tweetId] = self.count

    def getNewsFeed(self, userId: int) :
        timeList = []
        totalTweets = []
        totalTweets += self.tweets[userId]
        for followee in self.follows[userId]:
            totalTweets.extend(self.tweets[followee])

        unique = set(totalTweets)
        for tweet in unique:
            timeList.append((tweet, self.time[tweet]))
        timeList.sort(key=lambda x:x[1], reverse=True)
        res = []
        for item, time in timeList:
            res.append(item)
        if len(res) > 10:
            return res[:10]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        l = self.follows[followerId]
        if followeeId in l:
            l.remove(followeeId)
            self.follows[followerId] = l