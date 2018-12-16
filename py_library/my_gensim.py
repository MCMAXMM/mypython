raw_corpus = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
stoplist = set('for a of the and to in'.split(' '))
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in raw_corpus]

from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

precessed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
print(precessed_corpus)
from gensim import corpora

dictionary = corpora.Dictionary(precessed_corpus)
# print(dictionary)
#Dictionary(12 unique tokens: ['computer', 'human', 'interface', 'response', 'survey']...)
#print(dictionary.token2id)
#打印出一个word2id的字典
#{'computer': 0, 'human': 1, 'interface': 2, 'response': 3, 'survey': 4, 'system': 5, 'time': 6, 'user': 7, 'eps': 8, 'trees': 9, 'graph': 10, 'minors': 11}

#下面是词袋bag of words表示
new_doc = "human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)
#[(0, 1), (1, 1)] 元组（id,频率）由于interaction没有在dictionary中出现，所以只有两个
bow_corpus = [dictionary.doc2bow(text) for text in precessed_corpus]
print(bow_corpus)
#tf-idf
from gensim import models
tfidf = models.TfidfModel(bow_corpus)
string = "system minors"
string_bow = dictionary.doc2bow(string.lower().split())
string_tfidf = tfidf[string_bow]
#tf-idf模型把词袋表达的向量转换到另一个向量空间，这个向量空间中，词频是根据语料中每个词的相对稀有程度（relative rarity）进行加权处理的。
print(string_bow)
#[(5, 1), (11, 1)]
print(string_tfidf)
#[(5, 0.5898341626740045), (11, 0.8075244024440723)]
