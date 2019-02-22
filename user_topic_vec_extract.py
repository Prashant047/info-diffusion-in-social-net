import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import tweepy
import csv
from tweet_crawler import get_tweets
from gensim import models, corpora
from scipy import spatial

consumer_key = '32kPBCxkpRdjftbA2aNIPz41b'
consumer_secret = 'YmfYen0Brw8FvUQMHZwNAfFXfopgTECti7nsq42KDXmIKzCxvg'
access_token = '748180615669891072-ofAuXoBlstCSlmMbYhtobGLNXfLchY4'
access_token_secret = 'qiyq0WzOjuG8tuhGggaF2tr3dLhfUYkJ0LJHs2zF54C4u'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def user_topic_vector(username, api):
    dictionary_path = '<_path_to_dictionary>'
    corpus_path = '<_path_to_corpus_>'

    dictionary = corpora.Dictionary.load(dictionary_path)
    corpus = corpora.MmCorpus('./corpus/{}.mm'.format(name))
    print('Dictionary and Corpus Loaded')

    user_tweets = get_tweets(username, api)
    print('Saved user {} tweets'.format(username))

    lda = models.LdaMulticore(corpus, id2word=dictionary, num_topics=2, passes=2, workers = 2)
    lda = lda.load('<model_path>')
    print('LDA_Model loaded')

    user_tweets = ' '.join(user_tweets)
    vec_bow = dictionary.doc2bow(user_tweets.lower().split())
    vec_lda = lda[vec_bow]

    return vec_lda

def cosin_distance(topic_vec1, topic_vec2):
    return spatial.distance.cosine(topic_vec1, topic_vec2)













