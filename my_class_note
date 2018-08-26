# def line_config(content,length):
#     def line():
#         print("-"*(length//2)+content+"-"*(length//2))
#     return line#就把函数当成类似于整数的参数，只不过他有可以被调用的性质，可以被外面调用
# line=line_config("helafd",23)
# line()
# line()
# line()
#闭包是函数以及他的上下文环境
# def test():
#     num=10
#     def test2():
#         nonlocal num
#         num=12
#         print(num)
#     return test2
# result=test()
# result()
# def test1(func):
#     def inner():
#         print("hello world")
#         func()
#     return inner
# @test1
# def test2():
#     print("hello machao")
# test2()

#最外层带有参数的装饰器
# def get_decorator(char):
#   def decorator(func):
#     def decorated(*args,**kwargs):
#       print(char*20)
#       res=func(*args,**kwargs)
#       return res
#     return decorated
#   return decorator
# @get_decorator("*")
# def test2(num1,num2):
#   print("hello world")
#   sum=num1+num2
#   return sum
# res=test2(2,3)
# print(res)

#生成器
# def gen():
#     for i in range(10):
#         yield i
# a=gen()
# for i in range(11):
#     try:
#         print(a.__next__())
#     except Exception:
#         print("出现越值异常")
#     finally:
#         pass

#递归调用
# def my_sorted(data,sorted_data=[]):
#     if len(data)==1:
#         return [data]
#     else:
#         sorted_data.append(max(data))
#         data.remove(max(data))
#         my_sorted(data)
#     return sorted_data
# a=my_sorted([3,4,1,2,3,213,123123,2,5,6])
# print(a)


#关于os的操作
# import os
# import shutil
# print(os.getcwd())
# shutil.move
# class person():
#     pass
# a=person()
# a.age=3
# #在后面打一个.print就可把前面的东西加到print当中
# print(a.__dict__)#dict 里面存储的是对象属性的字典
# print(person.__dict__)
# #对象增加属性和类增加属性是有区别的
# a.height=12
# print(a.height)
# del a.height
# try:
#     print(a.height)
# except Exception:
#     print("出现异常"
#           #万物皆对象，类也是对象
# class person:
#     def __init__(self):
#         self.age=12
#         height=12
#     name="das"
# print(person.__dict__)
# a=person()
# # print(a.__dict__)
# class one:
#     age=12
# a=one()
# a.age=13
#     name="hfasdf"
# a.__dict__["age"]=15
# print(a.__dict__)
# one.__dict__["age"]=145
# print(one.age)
# #对象的属相可以通过__dict__字典来修改，但是类却不能直接通过__dict__来修改类属性
#实例方法，类方法，静态方法依据方法的第一个参数的类型来划分
#方法实际存储在类对象里面而不是实例对象里面
# class person:
#     def eat(self):
#         print("这是一个实例方法",self)
#     @classmethod#定义一个列方法，加上一个类装饰器
#     def leifangfa(cls):
#         print("this is a class function",cls)
#     @staticmethod
#     def jingtaifangfa():
#         print("this is a static function")
# # p=person()
# # p.eat()
# # print(p)
# print(person.__dict__)
# p=person()
# print(p.__dict__)
# a=[1,2,34]
# print(a.__class__)

# print(int.__class__)
# def run(self):
#     print("hello world")
# dog=type("dag",(),{"name":"chaobo","run":run})
# b=dog()
# print(dog.__dict__)
# class person:
#     __metaclass__=type
# class person:
#     def __init__(self):
#         self.__age=10
#     #可以使用属性的方式来调用方法
#     @property
#     def age(self):
#         return self.__age
#
# print(person().age)
# #经典类没有继承object，新式类继承object
# print(person.__bases__)
#property的第一种使用方式
# class person:
#     def __init__(self):
#         self.__age=18
#     def get_x(self):
#         return self.__age
#     def set_x(self,value):
#         self.__age=value
#     age=property(get_x,set_x)
# a=person()
# a.age=12
# print(a.age)
#property的第二种使用方式
# class person:
#     def __init__(self):
#         self.__age=10
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         self.__age=value
# a=person()
# print(a.age)
# a.age=12
# print(a.age)

# class person:
#     #当我们给一个实例增加属性或修该属性时，都会调用这个方法
#     #在这个方法内部，才会真正的属性和其对应的值写到__dict__中
#     def __setattr__(self, key, value):
#         print(key,value)
#         if key =="age" and key in self.__dict__.keys():#这段代码时关于只读属性的编写
#             print("这个属性是只读属性，不能添加到类中")
#         else:
#             self.__dict__[key]=value
#             #不能使用self.key=value否则会递归调用
# p1=person()
# p1.age=12
# print(p1.__dict__)
# p1.name=12
# print(p1.name)

#系统常用的内置属性
# class person:
#     """
#     this is a person
#     """
#     def __init__(self):
#         self.name="sz"
#     def run(self):
#         print("run")
# print(person.__dict__)#输出类的所有属性，以字典形式返回
# print("#"*30)
# print(person.__bases__)#输出类的所有父类组成的元组
# print(person.__doc__)#输出这个类的文档内容
# print(person.__name__)#输出这个类的名字
# print(person.__module__)#查看一下类定义所在的模块，这次输出的是主模块
# p=person()
# print(p.__class__)#查看一下实例所在的类

#私有化方法
# class person:
#     __age=10
#     def __run(self0):
#         print("hello world")
# p=person()
# print(person.__dict__)
# p.__run()
#面向对象内置特使方法，上面为内置属性要区分开来
#内置特殊方法分为生命周期方法和其他内置方法

#1.信息格式化操作 __str__方法和__repr__方法
# class person:
#
#     def __init__(self):
#         self.name="hello"
#         self.age=12
#     def __str__(self):#面向的是用户，而__repr__面向的是开发人员，Python解释器
#         return "name={},age={}".format(self.name,self.age)
#     #要想打出str信息要么调用str函数，或者print（对象实例）
#     def __repr__(self):#使用repr函数或者交互界面打出对象实例后+enter
#         return "repr"
# p1=person()
# print(p1.name)
# print(p1.age)
# print(p1)
# s=str(p1)
# print(s)
# print(repr(p1))#获取p1的本质信息而不是调用str
#举个例子
# import datetime
# t=datetime.datetime.now()
# print(t)#调用__str__方法面向用户
# print(repr(t))#调用__repr__方法面向开发人员
# tmp=repr(t)
# result=eval(tmp)
# print(result)


#__call__方法
# class person:
#     def __call__(self, *args, **kwargs):
#         print("hello world")
#         print(args)
#         print(kwargs)
#     pass
# p=person()
# p(1223,2312,name=12)
# class penfactory:
#     def __init__(self,type):
#         self.type=type
#     def __call__(self,pcolor):
#         print("创建一个%s这个类型的画笔，它是%s颜色"%(self.type,pcolor))
# gangbif=penfactory("钢笔")#type变化类型少，color变化类型多
# gangbif("红色")
# gangbif("绿色")
# gangbif("黄色")


#索引操作
#作用可以将我们创建好的实例对象可以以列表或字典的形式进行操作
#有三个内置方法分别实现增、改，查，删
# class person:
#     def __init__(self):
#         self.cache={}
#     def __setitem__(self, key, value):
#         #print("setitem",key,value)
#         self.cache[key]=value
#     def __getitem__(self, item):
#         #print("getitem",item)
#         return self.cache[item]
#     def __delitem__(self, key):
#         #print("delitem",key)
#         del self.cache[key]
# p=person()
# p["name"]="hello"#setitem
# print(p["name"])#getitem
# del p["name"]#delitem
# print(p["name"])


#切边操作
# class person:
#     def __init__(self):
#         self.items=[12,3,4,123,2342,23,12324]#切片操作只能去修改，而不能新增
#         #需要你手动去写
#     def __setitem__(self, key, value):#这个key值是一个切片对象
#         # print(key,value)
#         # print(key.start)
#         # print(key.stop)
#         # print(key.step)
#         # print(value)
#         if isinstance(key,slice):#防止与索引操作冲突，有可能传进来的key值是字符串
#             self.items[key]=value
#     def __getitem__(self, item):
#         print("getitem",item)
#     def __delitem__(self, key):
#         print("del item",key)
# p=person()
# p[0:4:2]=["sa","afa"]
# print(p.items)
# print(isinstance(slice(0,4,2),slice))#切片对象
# del p


#比较操作
# class person:
#     def __init__(self,age,height):
#         self.age=age
#         self.height=height
#     #==,!=,>,<,>=,<=
#     def __eq__(self, other):
#         return self.age==other.age#判断等于和不等于时，编写一个等于就行，系统会自动推导不等于的情况，剩下类似
#     def __ne__(self, other):
#         return self.age!=other.age
#     def __gt__(self, other):#>这边的比较符号不能叠加
#         pass
#     def __ge__(self, other):#>=
#         pass
#     def __lt__(self, other):#<
#         pass
#     def  __le__(self, other):#<=
#         pass
#
# p1=person(12,123)
# p2=person(13,123)
# print(p1==p2)
# print(p1!=p2)
#方案二也可以调用functools装饰器，让它自动补全它反方向的操作
# import functools
# @functools.total_ordering
# class person:
#     def __lt__(self, other):
#         pass
#     def __eq__(self, other):
#         pass
# p1=person()
# p2=person()
# print(person.__dict__)
# print(p1==p2)

# class person:
#     def __init__(self):
#         self.data=9
#     def __bool__(self):
#         return self.data>=10
# p=person()
# if p:
#     print("hello")
# else:
#     print("world")


#便利操作或迭代操作
#第一种使用getitem方法
# class person:
#     def __init__(self):
#         self.result=1
#     def __getitem__(self, item):
#         self.result+=1
#         if self.result>=6:
#             raise StopIteration("停止遍历")
#         return self.result
#     pass
# p=person()
# for i in p:
#     print(i)

#方式二
# class person:
#     def __iter__(self):
#         #return iter([1,2,3,4,5,56,6])
#         return self
#     def __next__(self):
#         self.result+=1
#         if self.result>=6:
#             raise StopIteration("停止遍历")
#         return self.result
# p=person()
# for i in p:#这边的p指的是iter方法返回的可迭代对象,如果返回的是self,则它会去调用next
#     #可以使用next每次返回一个数据
#     print(i)
#一个迭代器肯定可以通过一个next函数来访问，但是能访问不一定是迭代器，必须有iter方法和next方法

# #迭代器的复用，需要在iter方法里面初始化他的终止条件
# class person:
#     def __init__(self):
#         self.age=1
#     def __iter__(self):
#         self.age=1#重新将age初始化为1，使用for in person时iter只调用一次，剩下就是next
#         return self
#     def __next__(self):
#         self.age+=1
#         if self.age>6:
#             raise StopIteration("越过limit了")
#         return self.age
# p=person()
# for i in p:
#     print(i)
# print("")
# for i in p:
#     print(i)
# import collections
# print(isinstance(p,collections.Iterator))#判定一个东西是否为迭代器，实现两个方法才行
# print(isinstance(p,collections.Iterable))#实现一个方法即__iter__方法就行


#描述器
#作用，可以对数据进行过滤，要实现三个方法__set__,__get__,__delete__
#实现方式一
# class person:
#     def __init__(self):
#         self.__age=10
#     def get_age(self):
#         return self.__age
#     def set_age(self,value):
#         if value<0:
#             value=0
#         self.__age=value
#     def del_age(self):
#         del self.__age
#     age=property(get_age,set_age,del_age)
# p=person()
# print(p.age)
# #描述器实现方式二
# class person:
#     def __init__(self):
#         self.__age=10
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if value<0:
#             value=0
#         self.__age=value
#     @age.deleter
#     def age(self):
#         del self.__age
# p=person()
# print(p.age)
# print(p.__dict__)
#上面的实现方式过于麻烦，一个属性就要实现三个方法，要是多个属性的话就会很复杂
# class age:
#     def __get__(self, instance, owner):
#         print("get")
#     def __set__(self, instance, value):
#         print("set")
#     def __delete__(self, instance):
#         print("delete")
# class person:
#     age=age()
# # p=person()
# # print(p.age)
# # p.age=12
# # del p.age
# print(person.age)#以后是以实例操作，而不是用类来操作，描述器只能在新式类中生效，即继承自object
# person.age=12
# del person.age

#使用类来实现装饰器
# class check:
#     def __init__(self,func):
#         self.func=func
#     def __call__(self, *args, **kwargs):
#         print("nihao")
#         self.func()
# @check
# def fashuoshuo():
#     print("hello world")
# fashuoshuo()
# class deco:
#     def __init__(self,func):
#         self.func=func
#     def __call__(self,*args,**kwargs):
#         print("hello world")
#         result=self.func(*args,**kwargs)
#         return result
# @deco
# def sum(n1,n2):
#     return n1+n2
#
# a=sum(2,3)
# print(a)
# #继承的意思是可以使用父类的东西，并不是创建新的东西
# print(deco.__mro__)
# class a():
#     @classmethod
#     def pr(self):
#         print("hello world")
# a.pr()
# a=a()
# a.pr()
# class a():
#     def __init__(self):
#         self.a=3
# class b(a):
#     def __init__(self):
#         super().__init__()
#         self.b=2
# a=b()
# print(a.a)
#抽象类的编写
import abc
class person(object,metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def print1(self):
        pass
