import sys

import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer

from twitter_bot import create_api

api = create_api()
sid = SentimentIntensityAnalyzer()

def read_tweet_replies(content):
    with open("replies.txt", "w") as tweet_file:
        new_tweets = api.user_timeline(screen_name="AnonymousBot15")
        for tweet in new_tweets:
            if tweet.text == content:
                replies = tweepy.Cursor(api.search, q='to:{}'.format("AnonymousBot15"),
                                        since_id=tweet.id, tweet_mode='extended').items()
                for reply in replies:
                    tweet_file.write(str(reply.full_text+","+max(sid.polarity_scores(str(reply.full_text)),key=sid.polarity_scores(str(reply.full_text)).get))+"\n")
    tweet_file.close()

if __name__ == '__main__':
    file = open("content.txt")
    content = file.read().strip()
    read_tweet_replies(content)