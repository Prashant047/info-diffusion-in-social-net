import logging
from gensim import corpora
from collections import defaultdict
from pprint import pprint
import csv
import re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def make_corpus_from_user_tweets(name):
    open('./corpora_dicts/{}.dict'.format(name), 'a').close()
    open('./corpus/{}.mm'.format(name), 'a').close()

    documents = []

    with open('./user_tweets/{}.csv'.format(name)) as input_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        for i, row in enumerate(csv_reader):
            text = row[0]
            url_regex = 'https://t.co/[\w]*'
            tag_regex = '@[\w]*'
            b_code = '[\w]*(\\x[\w]{2})[\w]*'

            urls = re.findall(url_regex, text)
            tags = re.findall(tag_regex, text)
        

            for url in urls:
                text = text.replace(url, '')
            for tag in tags:
                text = text.replace(tag, '')
            text = text.replace('RT : ', '')
            text = text.replace("\n", '')

            documents.append(text)

    # print(documents[:10])

    stop_word_list = [
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", 
        "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
        "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
        "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", 
        "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", 
        "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
        "for", "with", "about", "against", "between", "into", "through", "during", "before", 
        "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", 
        "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", 
        "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", 
        "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", 
        "don", "should", "now"
    ]

    stop_word_list_hindi = [
        "अंदर","अत","अदि","अप","अपना","अपनि","अपनी","अपने","अभि","अभी","आदि","आप","इंहिं",
        "इंहें","इंहों","इतयादि","इत्यादि","इन","इनका","इन्हीं","इन्हें","इन्हों","इस","इसका","इसकि","इसकी","इसके","इसमें","इसि",
        "इसी","इसे","उंहिं","उंहें","उंहों","उन","उनका","उनकि","उनकी","उनके","उनको","उन्हीं","उन्हें","उन्हों","उस","उसके","उसि","उसी",
        "उसे","एक","एवं","एस","एसे","ऐसे","ओर","और","कइ","कई","कर","करता","करते","करना","करने","करें","कहते","कहा","का",
        "काफि","काफ़ी","कि","किंहें","किंहों","कितना","किन्हें","किन्हों","किया","किर","किस","किसि","किसी","किसे","की","कुछ","कुल","के",
        "को","कोइ","कोई","कोन","कोनसा","कौन","कौनसा","गया","घर","जब","जहाँ","जहां","जा","जिंहें","जिंहों","जितना","जिधर","जिन",
        "जिन्हें","जिन्हों","जिस","जिसे","जीधर","जेसा","जेसे","जैसा","जैसे","जो","तक","तब","तरह","तिंहें","तिंहों","तिन","तिन्हें","तिन्हों",
        "तिस","तिसे","तो","था","थि","थी","थे","दबारा","दवारा","दिया","दुसरा","दुसरे","दूसरे","दो","द्वारा","न","नहिं","नहीं","ना","निचे",
        "निहायत","नीचे","ने","पर","पहले","पुरा","पूरा","पे","फिर","बनि","बनी","बहि","बही","बहुत","बाद","बाला","बिलकुल","भि","भितर","भी",
        "भीतर","मगर","मानो","मे","में","यदि","यह","यहाँ","यहां","यहि","यही","या","यिह","ये","रखें","रवासा","रहा","रहे","ऱ्वासा","लिए","लिये",
        "लेकिन","व","वगेरह","वरग","वर्ग","वह","वहाँ","वहां","वहिं","वहीं","वाले","वुह","वे","वग़ैरह","संग","सकता","सकते","सबसे","सभि",
        "सभी","साथ","साबुत","साभ","सारा","से","सो","हि","ही","हुअ","हुआ","हुइ","हुई","हुए","हे","हें","है","हैं","हो","होता","होति",
        "होती","होते","होना","होने"
    ]

    combined_stop_word_list = stop_word_list + stop_word_list_hindi
    # print(combined_stop_word_list)

    stop_list = set(combined_stop_word_list)
    texts = [[word for word in document.lower().split() if word not in stop_list]
        for document in documents]
    # print(texts[:5])

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1]
            for text in texts]

    # pprint(texts[:5])
    dictionary = corpora.Dictionary(texts)
    dictionary.save('./corpora_dicts/{}.dict'.format(name))

    # print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('./corpus/{}.mm'.format(name), corpus)
    print('corpus saved in ./corpus/{}.mm'.format(name))

make_corpus_from_user_tweets('sirajraval')
