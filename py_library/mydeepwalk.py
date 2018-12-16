import random
from deepwalk import graph
from gensim.models import Word2Vec
#1.第一步导入图
G = graph.load_matfile("./blogcatalog.mat")
print(G.values())
print("Number of nodes: {}".format(len(G.nodes())))
num_walks = len(G.nodes()) * 10#(每个节点随机游走的数目)
print("Number of walks: {}".format(num_walks))
data_size = num_walks * 40#游走长度
print("Data size (walks*length): {}".format(data_size))
#2.开始游走
walks = graph.build_deepwalk_corpus(G, num_paths=10,
                                    path_length=40, alpha=0, rand=random.Random(0))
#3转化为向量
model = Word2Vec(walks, size=64, window=5, min_count=0, sg=1, hs=1, workers=1)
#前面那种适用于数据小的模式
#数据量大的需要写到硬盘
