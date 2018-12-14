# import multiprocessing as mp

# 1.和多线程差不多
# def job(q):
#     print("hello world")
#     res=0
#     for i in range(1000):
#         res+=i+i**2+i**3
#     q.put(res)
# if __name__=="__main__":
#      #一定要在main下执行，否则就会报错
#
#     q=mp.Queue()#它不像thread他用的自带的queue
#     p1 = mp.Process(target=job, args=(q,))#args如果只有一个值，要带个逗号
#     p2=mp.Process(target=job,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1=q.get()
#     res2=q.get()
#     print(res1+res2)


#2.进程池pool
# import multiprocessing as mp
# def job(x):
#     return x*x
# def multicore():
#     pool=mp.Pool(processes=3)#使用进程池获得返回值，它会自动调用内核
#     #map的话它会自动将任务分配给多个进程
#     res=pool.map(job,range(100))
#     #res=pool.apply_async(job,(2,))#只能输入一个值
#     #apply_async一次只能分配一个进程，你可以使用迭代器的方式分配多个进程
#     multi_res=[pool.apply_async(job,(i,))for i in range(10)]
#     print([res.get() for res in multi_res])
#     print(res)
# if __name__=="__main__":
#     multicore()
#
# #共享内存，各个核之间的内存是不共享的(变量)，所以需要共享变量
# import multiprocessing as mp
# value=mp.Value('d',1)
# array=mp.Array("i",[1,2,3])


#3.lock和共享内存
import multiprocessing as mp
import time
def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value+=num
        print(v.value)
    l.release()
def multicore():
    v=mp.Value("i",0)
    l=mp.Lock()
    p1=mp.Process(target=job,args=(v,1,l))
    p2=mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
if __name__=="__main__":
    multicore()
