import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import gensim
from gensim import corpora, models, similarities

ml_text = ['/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/classification.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/clustering.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/dimensionality_reduction.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/regression.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/supervised_learning.txt']


network_text = ['/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/basics.txt',
                '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/data_link_layer.txt',
                '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/network_layer.txt',
                '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/physical_Layer.txt']

stop_words = stopwords.words('english')
stop_words.extend(
    ['news', 'say', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'took',
     'time',
     'year',
     'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack',
     'make',
     'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come', 'new', 'said',
     'like', 'people'])

stemmer = PorterStemmer()

for file in network_text:
    with open(file, 'r') as f:
        text = f.read()
        f.close()
    tokenized = nltk.word_tokenize(text)
    tokenized = [stemmer.stem(word) for word in tokenized]
    tokenized = [[word for word in tokenized if len(word) > 1]]
    dictionary = corpora.Dictionary(tokenized)
    corpus = [dictionary.doc2bow(tokens) for tokens in tokenized]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)
    topics = ldamodel.print_topics(num_words=3)
    i = 1
    print('--------------------------------------------------')
    print(f'Topic modelling for the files {file} ')
    for topic in topics:
        print(f'topic {i} = {topic}')
        i += 1
