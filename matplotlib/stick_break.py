import matplotlib.pyplot as plt
import numpy as np
#my stick breaking sampling
#dp~dp(alpha,gaussian(0,1))
def stick_breaking(alpha,sample_num):
    x_list=[]
    y_list=[]
    for x in range(sample_num):
        data_x=np.random.normal(0,1,1)
        beta=np.random.beta(1,alpha,1)
        y=(1-sum(y_list))*beta
        x_list.append(data_x)
        y_list.append(y)
    return x_list,y_list
alpha=1000
sample_num=1000
x_list,y_list=stick_breaking(alpha,sample_num)
plt.stem(x_list,y_list)
plt.show()
