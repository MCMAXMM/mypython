#this file is to describe the generator
#生成器创建方式
#方法一
a=(l for l in range(100) if l%2==0)
print(next(a))
print(a.__next__())
#方法二,利用yield创建
def gen():
    for i in range(10):
        yield i#每次执行到yield i 就暂停，yield语句在这里可以当成return
g=gen()
for i in range(11):
    try:
        print(g.__next__())
        #print(next(g))
    except Exception:
        print("出现越值异常")
    finally:
        pass
#生成器的send()方法
#send()方法有一个参数，指定的上一次别挂起的yield语句的返回值
#相当于.__next__() 可以额外的给yield 传值
#注意第一次使用调用，要用.send(None)
def gen2():
  print("hello world")
  res1=yield 1
  print(res1)
  res2=yield 2
  print(res2)
g=gen2()
print(g.send(None))#send()会给上次挂起的yield赋值，但是第一次启动时没有yield所以需要传一个None值
