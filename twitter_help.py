import tweepy
import codecs

"""
Simple stuff for making it easier to play around with twitter.
"""

def auth()

    #Handles authentication.

    api_key = ""
    api_secret = ""
    access_token = ""
    access_secret = ""

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    global api
    api = tweepy.API(auth, wait_on_rate_limit = True)

def collect_tweets(user):

    #Collects tweets from specific user, txtfile output.

    tweets = tweepy.Cursor(api.user_timeline, id=user).items()

    with codecs.open("output.txt", "w+", "utf-8") as output:

        for tweet in tweets:
            output.write(tweet.text+"\n")

def publish_tweet(string):

    #For actual tweeting!

    api.update_status(status=string)


if __name__ == '__main__':
    pass
