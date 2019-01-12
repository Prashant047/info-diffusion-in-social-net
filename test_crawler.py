import tweepy
import time
import json

consumer_key = '32kPBCxkpRdjftbA2aNIPz41b'
consumer_secret = 'YmfYen0Brw8FvUQMHZwNAfFXfopgTECti7nsq42KDXmIKzCxvg'
access_token = '748180615669891072-ofAuXoBlstCSlmMbYhtobGLNXfLchY4'
access_token_secret = 'qiyq0WzOjuG8tuhGggaF2tr3dLhfUYkJ0LJHs2zF54C4u'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# def calc_run_time(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrapper


def get_tweets(username, api):
    # MAX 3240 tweets - Restricted by Twitter
    start_time = time.time()
    retweet_count = 0
    all_tweets=[]  
    upper_page_limit = 167

    for x in range(1, upper_page_limit):
        tweets = api.user_timeline(screen_name=username, page=x, tweet_mode="extended") 
        if len(tweets) == 0:
            break
        tweets_for_csv = [tweet for tweet in tweets] # CSV file created  
        for t in tweets_for_csv:
            text = t.full_text
            start_tag = text[:3]
            if start_tag == 'RT ':
                retweet_count = retweet_count + 1
            
            all_tweets.append(t)  

    end_time = time.time()
    # print('Run time: {}'.format(int(end_time-start_time)))

    return all_tweets, len(all_tweets), retweet_count




def get_followers(username, api):
    current_user = api.get_user(username)
    users = []
    page_count = 0

    try:
        for user in tweepy.Cursor(api.followers, id=current_user.id, count=300).pages():
            page_count = page_count + 1
            print('Getting page {} for followers'.format(page_count))
            users.extend(user)

        return users
    except tweepy.error.RateLimitError:
        return users

def get_followers_count(username, api):
    user = api.get_user(username)
    return user.followers_count


def get_friends_count(username, api):
    user = api.get_user(username)
    return user.friends_count

def num_d_rtweets_s(s, d, tweets):
    num_rtweets = 0
    for tweet in tweets:
        text = tweet.full_text
        tag = text[:3]

        if tag == 'RT ':
            screen_name1 = tweet._json['retweeted_status']['in_reply_to_screen_name']
            screen_name2 = tweet._json['entities']['user_mentions']
            if len(screen_name2) == 0:
                screen_name2 = ''
            else:
                screen_name2 = screen_name2[0]['screen_name']
     
            if screen_name1 == d or screen_name2 == d:
                num_rtweets = num_rtweets + 1

    return num_rtweets


tweets, no_of_tweets, no_of_rtweets = get_tweets('yashsoni_27  ', api)
# print(num_d_rtweets_s('yashsoni_27 ', 'sirajraval', tweets))
# print(tweets[17]._json)

r = tweets[0]._json
r = json.dumps(r)
print(r)
# loaded_r = json.loads(r)

