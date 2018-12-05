import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(0,60,2).reshape(10,3),columns=list('abc'))
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                       'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                      'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
# # 1.查看数据类型
# print(df2.dtypes)
# # 2.查看头部，或者尾部的数据
# print(df2.head(3))
# print(df2.tail(3))
# # 3.查看index，columns,和values
# print(df2.index,df2.columns,df2.values)
# # 4.查看数据的快速统计信息
# print(df2.describe())
# # 5.转置和排序
# print(df.T)
# print(df2.sort_index(axis=1,ascending=False))#ascending是升序的意思
# print(df2.sort_values(by='C'))
