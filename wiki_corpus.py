from gensim.test.utils import datapath, get_tmpfile
from gensim.corpora import WikiCorpus, MmCorpus

path_to_wiki_dump = '/Volumes/Segate/enwiki-latest-pages-articles.xml.bz2'

# for text in WikiCorpus(path_to_wiki_dump).get_texts():
#     if i == 5:
#         break
#     print(text)
#     i = i+1

def make_corpus(in_f, out_f):

	"""Convert Wikipedia xml dump file to text corpus"""

	output = open(out_f, 'w')
	wiki = WikiCorpus(in_f)

	i = 0
	for text in wiki.get_texts():
		output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
		i = i + 1
		if (i % 100 == 0):
			print('Processed ' + str(i) + ' articles')
	output.close()
	print('Processing complete!')

def init_dictionary(path_to_wiki_dump):
	print('Dictionary initilization started...')

	wiki = WikiCorpus(datapath(path_to_wiki_dump))
	wiki.init_dictionary()

	print('Done Bitch!!!!!')


# make_corpus(path_to_wiki_dump, 'wiki_en.txt')
init_dictionary(path_to_wiki_dump)





