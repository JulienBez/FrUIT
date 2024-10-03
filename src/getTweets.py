import tweepy
from .manageFile import *

API_KEY = 'your-api-key'
API_SECRET = 'your-api-secret'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

def authentification():
    """authentification to Twitter API"""
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


def getTweetData(tweet_id,tweet):
    """create a well-formated data format for each tweet"""
    return {
        "tweet": tweet.user.id_str,
        "metadata": {
            "id": tweet_id["id"],
            "user": tweet.user.id_str,
            "created_at": tweet.created_at.split("T")[0],
            "retweet_count": tweet.retweet_count
            },
        "parenté": {
            "seed": tweet_id["seed"],
            "distance": tweet_id["distance"]
            }
        }


def getTweets():
    """fetch tweets according to our list of ids via Twitter API"""
    createFolder("data/tweets")
    api = authentification()
    tweets_ids = openJson("data/tweets_ids.json")
    tweets = []
    counter = 0
    for tweet_id in tqdm(tweets_ids):
        try:
            tweet = api.get_status(tweet_id["id"], tweet_mode='extended')
            entry = getTweetData(tweet_id,tweet)
        except tweepy.TweepError as e:
           print(f"Error: {e}")
        if len(tweets) < 10000:
            tweets.append(entry)
        else:
            writeJson(f"data/tweets/{counter}.json",tweets)
            tweets = [entry]
            counter += 1
    if len(tweets) > 0:
        writeJson(f"data/tweets/{counter}.json",tweets)
    
