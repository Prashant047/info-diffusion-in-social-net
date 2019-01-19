import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities
import os
import re

something = "(0\.[0-9]*)\*\"([a-z\']*)\""

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

    lda = models.LdaMulticore(corpus, id2word=dictionary, num_topics=2, passes=2, workers = 2)

    """
        To save the model
            temp_file = datapath("model")
            lda.save(temp_file)
        To load a saved model
            lda = LdaModel.load(temp_file)

    """

    # print('----------------END-----------------')
    # s = re.findall(something, str(lda.print_topics()))
    # print(s)

    for idx, topics in lda.print_topics(-1):
        print("Topic: {} ------------>".format(idx))
        print(topics)


lda('sirajraval')
