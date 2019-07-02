from collections import namedtuple
#带有名字的元组，数据不可修改，像字典一样具有可读性
human=namedtuple("human","name age")
chaobo=human(name="chaobo",age=31)
print(chaobo)
print(chaobo.name)
