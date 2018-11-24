import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
global LEN
LEN=1000
rv=stats.dirichlet.rvs([1,1,1],30000)
rvs=rv[:,0:2]
list=[]
for x in rv:
    pdf=stats.dirichlet.pdf(x,alpha=[1,10,21])
    list.append(float(pdf))
fig=plt.figure()
ax=fig.gca(projection="3d")
ax.scatter(rvs[:,0],rvs[:,1],list)
plt.show()
