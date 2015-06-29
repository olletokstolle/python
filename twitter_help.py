import tweepy
import codecs

def auth():
    #handles authentication

    api_key = ""
    api_secret = ""
    access_token = ""
    access_secret = ""

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    global api
    api = tweepy.API(auth, wait_on_rate_limit = True)

def collect_tweets(user):
    #collects tweets from specific user, txtfile output.

    tweets = tweepy.Cursor(api.user_timeline, id=user).items()

    with codecs.open("output.txt", "w+", "utf-8") as output:

        for tweet in tweets:
            output.write(tweet.text+"\n")

def publish_tweet(string):
    #for actual tweeting

    api.update_status(status=string)


if __name__ == '__main__':
    pass
