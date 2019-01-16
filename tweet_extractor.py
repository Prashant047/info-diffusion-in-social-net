import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = '32kPBCxkpRdjftbA2aNIPz41b'
consumer_secret = 'YmfYen0Brw8FvUQMHZwNAfFXfopgTECti7nsq42KDXmIKzCxvg'
access_token = '748180615669891072-ofAuXoBlstCSlmMbYhtobGLNXfLchY4'
access_token_secret = 'qiyq0WzOjuG8tuhGggaF2tr3dLhfUYkJ0LJHs2zF54C4u'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def collect_tweets(hastag):
    csv_file = open('./collected_tweets/{}.csv'.format(hastag), 'a')
    csv_writer = csv.writer(csv_file)

    num_collected = 0
    for tweet in tweepy.Cursor(api.search,q="#{}".format(hastag),count=200,lang="en").items():
        # print(tweet.created_at, tweet.text)
        csv_writer.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        num_collected = num_collected + 1
        print(num_collected)

collect_tweets("politics")