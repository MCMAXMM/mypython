from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
from matplotlib import cm
#联合[0,1],[[1,1],[1,2]]
#边缘(0,1)
#条件在x_b=3条件下服从（1,0.5）
fig1=plt.figure()
ax=fig1.gca(projection="3d")
x1,x2=np.meshgrid(np.linspace(-6,6,1000),np.linspace(-6,6,1000))
x=np.stack((x1,x2),axis=2)
norm=stats.multivariate_normal(mean=[0,1],cov=[[1,1],[1,2]])
pdf_x=norm.pdf(x)
x_1=np.linspace(-5,5,200)
x_2=3*np.ones(200)
ax.plot_surface(x1,x2,pdf_x,cmap=cm.coolwarm)
fig=plt.figure()
pdf_marg=stats.norm(loc=0,scale=1).pdf(x_1)
pdf_cond=stats.norm(loc=1,scale=0.5).pdf(x_1)
plt.subplot(211)
plt.plot(x_1,pdf_marg)
plt.plot(x_1,pdf_cond)
plt.subplot(212)
plt.contour(x1,x2,pdf_x)
plt.plot(x_1,x_2)
plt.show()
