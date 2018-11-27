import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist,cdist,squareform
from scipy.optimize import minimize
#制造假数据
train_num=100
np.random.seed(1234)
x=np.random.random(train_num)*10
x=x.reshape(-1,1)
noise=np.random.normal(0,1,train_num).reshape(-1,1)
y=np.sin(x)
x_new=np.linspace(0,10,200).reshape(-1,1)
plt.plot(x_new,np.sin(x_new),c="red")
#真实的图像应该为
sigma_f=1
sigma_n=2
l=2
#总共只有三个参数
paraml=[sigma_f,l,sigma_n]
class Gaussian_process:
    def __init__(self, paraml):
        self.paraml=paraml
        self.sigma_f=paraml[0]
        self.l=paraml[1]
        self.sigma_n=paraml[2]
#计算kernel矩阵
    def kern_mat(self,x_train,x_new,paraml):
        if x_new is None:
            distance=squareform(pdist(x_train))
            ker_mat=paraml[0]*np.exp(-distance**2/(2*paraml[1]**2)+paraml[2]*np.identity(distance.shape[0]))
        else:
            distance=cdist(x_new,x_train)
            ker_mat=self.paraml[0]*np.exp(-distance**2/(2*self.paraml[1]**2))
        return ker_mat
    def neg_log_like(self,my_parm):

        K=self.kern_mat(x, x_new=None,paraml=my_parm)
        d= 0.5*self.train_y.T.dot(np.linalg.pinv(K)).dot(self.train_y)\
           +0.5*np.log(np.linalg.det(K))+0.5*np.shape(K)[0]*np.log(2*np.pi)
        d=np.squeeze(d)
        return d


    def train(self,train_x,train_y):
        self.train_x=train_x
        self.mean=np.mean(train_y,axis=0)
        self.train_y=train_y-self.mean
        bounds=[[-2,2],[0.1,2],[0.1,2]]
        res=minimize(self.neg_log_like,np.array(self.paraml),method='l-bfgs-b', tol=1e-12,)
        print("log likelihood is ",res.fun)
        print("res_x",res.x)
        print("参数为：",res.x)
        self.paraml=res.x
    def predict(self,train_x,train_y,x_new):
        K=self.kern_mat(x_train=train_x,x_new=None,paraml=self.paraml)
        K1=self.kern_mat(x_train=train_x,x_new=x_new,paraml=self.paraml)
        K11=self.kern_mat(x_train=x_new,x_new=None,paraml=self.paraml)

        mean=K1.dot(np.linalg.pinv(K)).dot(train_y)+np.mean(train_y)
        var=K11-K1.dot(np.linalg.pinv(K)).dot(K1.T)
        return mean,np.diagonal(var)
        # var=kk-Kk.dot(np.linalg.pinv(K)).dot(Kk.T)
        # error=np.diagonal(var)
        # return Kk.dot(np.linalg.pinv(K).dot(y))+mean,error
if __name__=="__main__":
    paraml=[0.72304537,1.13579686,0.78766707]
    #[0.87773639 1.22964691 0.69339147]144
    #[0.4194089  1.28820844 1.14695326]143
    gp=Gaussian_process(paraml)
    gp.train(x,y)
    mean,var=gp.predict(train_x=x,train_y=y,x_new=x_new)
    print(mean.shape)
    print(var.shape)
    plt.errorbar(x_new,mean,yerr=np.sqrt(var),color="green")
    print(var)
    plt.plot(x_new,mean,c="black")
    plt.show()
    


