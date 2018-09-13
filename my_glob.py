#glob是python自己带的一个文件操作相关模块，内容也不多，用它可以查找符合自己目的的文件，
#就类似于Windows下的文件搜索，而且也 支持通配符*,?,[]这三个通配符，代表0个或多个字符，
#*代表任意多个字符，?代表一个字符，[]匹配指定范围内的字符，如[0-9]匹配数字。
#glob方法： 返回所有匹配的文件路径列表，该方法需要一个参数用来指定匹配的路径字符串
#（本字符串可以为绝对路径也可以为相对路径），比如：
import glob
a=glob.glob(r"D:\pythonrun\20180504rnn\*.png")
print(a)
#output：
#['D:\\pythonrun\\20180504rnn\\image_at_epoch_0001.png', 'D:\\pythonrun\\20180504rnn\\image_at_epoch_0002.png',
'D:\\pythonrun\\20180504rnn\\image_at_epoch_0003.png', 
'D:\\pythonrun\\20180504rnn\\image_at_epoch_0004.png', 'D:\\pythonrun\\20180504rnn\\image_at_epoch_0005.png']
#返回的是一个列表
