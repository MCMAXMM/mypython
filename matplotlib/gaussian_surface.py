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


#方法2
import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
if __name__ == '__main__':
    x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]#类似于meshgrid,51j相当于有51个数
    x = np.stack((x1, x2), axis=2)
    # mpl.rcParams['axes.unicode_minus'] = False
    # mpl.rcParams['font.sans-serif'] = 'SimHei'
    plt.figure(figsize=(9, 8), facecolor='w')
    sigma = (np.identity(2), np.diag((3,3)), np.diag((2,5)), np.array(((2,1), (1,5))))
    for i in np.arange(4):
        ax = plt.subplot(2, 2, i+1, projection='3d')
        norm = stats.multivariate_normal((0, 0), sigma[i])
        y = norm.pdf(x)
        print(y.shape)
        ax.plot_surface(x1, x2, y, cmap=cm.Accent, rstride=2, cstride=2, alpha=0.9, lw=0.3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    plt.suptitle('二元高斯分布方差比较', fontsize=18)
    plt.tight_layout(1.5)
    plt.show()

