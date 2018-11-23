from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.gca(projection="3d")
x_data=np.linspace(-4,4,100)
y_data=np.linspace(-4,4,100)
def gaussian(x_data,y_data):
    X,Y=np.meshgrid(x_data,y_data)
    temp_x=np.reshape(X,(np.shape(X)[0]*np.shape(X)[1],1))
    temp_y = np.reshape(Y,(np.shape(Y)[0] * np.shape(Y)[1], 1))
    vector_x=np.concatenate((temp_x,temp_y),axis=1)
    list=[]
    sigma=np.array([[1,2],[0.3,2]])
    sigma_det=np.linalg.det(sigma)
    for x in vector_x:
        p=1/(2*np.pi*np.square(sigma_det))*np.exp(-0.5*np.matmul(np.matmul(x,sigma),x.reshape((2,1))))
        list.append(float(p))
    return list
list=gaussian(x_data,y_data)
X, Y = np.meshgrid(x_data, y_data)
Z=np.array(list).reshape(100,100)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.colorbar(surf)
plt.show()
