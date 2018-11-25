from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
data1=np.random.normal(0,2,30)
data2=np.random.normal(8,1,30)
zero=np.zeros((30,1))
d=stats.norm.pdf(np.linspace(-6,6,100),loc=0,scale=2)
e=stats.norm.pdf(np.linspace(5,11,100),loc=8,scale=1)
plt.plot(np.linspace(-6,6,100),d)
plt.plot(np.linspace(5,11,100),e)
plt.stem(data1,zero)
plt.stem(data2,zero)
plt.show()
