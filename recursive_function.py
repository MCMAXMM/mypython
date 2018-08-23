#this demo is about recursive function
#function调用其自身
#传递分为两个过程：传递和回归，类似于神经网络的前向传播和后向传播
def jiecheng(N):
  if N==1:
    return 1
  return N*jiecheng(N-1)
print(jiecheng(6))
# a sort demo
def my_sorted(data,sorted_data=[]):
    if len(data)==1:
        return [data]
    else:
        sorted_data.append(max(data))
        data.remove(max(data))
        my_sorted(data)
    return sorted_data
a=my_sorted([3,4,1,2,3,213,123123,2,5,6])
print(a)

