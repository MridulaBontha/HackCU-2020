import tweepy
import logging
import os
from twitter_keys import *
logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API")
        raise e
    print("API created")
    return api
