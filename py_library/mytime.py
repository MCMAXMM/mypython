import time
timestamp=1287503727
time_local=time.localtime(timestamp)
dt = time.strftime("%w-%H",time_local)#可以根据需求将时间解析成需要的格式
#上面解析为星期几和小时，星期是将周日编码为0
#lambda x:time.strftime("%w-%H",time.localtime(x)
