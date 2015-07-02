import tweepy
import codecs
import os
import random
import time

"""
Simple stuff for making it easier to play around with twitter.
"""

def auth():

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

    if len(string) <= 140:
        api.update_status(status=string)
    else:
        print("Could not tweet, string contained more than 140 chars.")
        print("error tweet: "+string)


def tweet_queue(txtfile, hour_interval):

    #Publishes tweets randomly picked from a textfile. Variables: txtfile (string), hour_interval (int).

    if os.path.isfile(txtfile) == False:
        print("File "+txtfile+" doesn't exist.")
        ok = False
    elif os.stat(txtfile).st_size == 0:
        print("File "+txtfile+" is empty.")
        ok = False
    else:
        ok = True

    while ok:

        with codecs.open(txtfile, "r+") as queue:

            lines = queue.readlines()
            tweet = random.choice(lines).replace("\n","")
            publish_tweet(tweet)

        #This part below removes the used tweet from the txtfile.

        with codecs.open(txtfile, "w+") as queue:

            queue.seek(0)

            if len(lines) > 1:

                for line in lines:
                    if line[-1:] == "\n":
                        if line != tweet+"\n":
                            queue.write(line)
                    else:
                        if line != tweet:
                            queue.write(line)
            else:
                queue.write("")


        time.sleep((60*60)*hour_interval)




if __name__ == '__main__':
    pass
