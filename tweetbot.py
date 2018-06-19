import tweepy
from random import randint, choice
import time

consumer_key = 'key'
consumer_secret = 'key'
access_token = 'key'
access_token_secret = 'key'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#main loop
while True:

    search = "ketchup"
    numberOfTweets = randint(1,4)

    choices = randint(1,4)

    #Retweeting Tweets
    if choices == 1:

        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.retweet()
                print('Retweeted the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    # Favoriting Tweets
    if choices == 2:

        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.favorite()
                print('Favorited the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    # Following Twitter User
    if choices == 3:

        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.user.follow()
                print('Favorited the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    if choices == 4:

        randomUpdates = ["update1",
                        "update2", "update3"]
        api.update_status(choice(randomUpdates))


    time.sleep(600)
