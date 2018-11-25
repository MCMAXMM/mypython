 import numpy as np
 x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]
 #x1的shape是[51,51],x2的shape是[51,51]
 x = np.stack((x1, x2), axis=2)
 #x的shape是[51,51,2],生成了新的轴，即第三个维度
 #但是np.concatenate只能在已有的维度上做连接
 print(x.shape)
 import numpy as np
data=np.identity(5)#[5,5]
data=np.expand_dims(data,axis=2)#[5,5,1]
print(data.shape)
data=np.squeeze(data,axis=2)#[5,5]
print(data.shape)
