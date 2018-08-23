# #装饰器的作用，函数的名字不用改变但是能够增加额外的功能
def decorator(func):
    def decorated(*args,**kwargs):#decorated等价于被装饰后的func,里面和外面的func要和最外面里面的参数要相同
        print("hello world")
        res=func(*args,**kwargs)
        return res
    return decorated
@decorator
def test1(num1,num2):
    sum=num1+num2
    return sum
a=test1(2,3)
print("a=%.5f"%a)
#装饰器装饰有参数的函数和有返回值的函数时都比较简单，但是
#装饰器在装饰有参数的装饰器时就比较麻烦
#下面就是一个这样的例子,它的装饰器里面带有参数
def get_decorator(char):
  def decorator(func):
    def decorated(*args,**kwargs):#decorated 应该和外面的test2和里面的func有相同的参数形式
      print(char*20)
      res=func(*args,**kwargs)
      return res#里面的func还应该和外面的test2有相同的返回形式
    return decorated
  return decorator
@get_decorator("*")
def test2(num1,num2):
  print("hello world")
  sum=num1+num2
  return sum
res=test2(2,3)
print(res)
