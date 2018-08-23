#this demo is about recursive function
#function调用其自身
#传递分为两个过程：传递和回归，类似于神经网络的前向传播和后向传播
def jiecheng(N):
  if N==1:
    return 1
  return N*jiecheng(N-1)
print(jiecheng(6))
