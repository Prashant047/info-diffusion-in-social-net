import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities
import os

dictionary = []
corpus = None

def lda(name):
    if os.path.exists('./corpora_dicts/{}.dict'.format(name)):
        dictionary = corpora.Dictionary.load('./corpora_dicts/{}.dict'.format(name))
        corpus = corpora.MmCorpus('./corpus/{}.mm'.format(name))

        print("Loaded!!!")
        print(corpus)
    else:
        print("Error!!!!")

    lda = models.LdaMulticore(corpus, id2word=dictionary, num_topics=1, passes=100, workers = 2)
    lda.print_topics()

lda('sirajraval')