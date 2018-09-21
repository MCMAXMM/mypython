#this demo is about file_operation#wen
#文件分为文本文件和二进制文件
# r 模式 以只读模式打开文件，文件的指针将会放在文件的开头，如果文件不存在就会报错
# w 模式 以只写模式打开文件，文件的指针将会放在文件的开头，完全覆盖式的写入，如果文件不存在就会创建新的文件
# a 以追加模式（只写）打开文件，文件的指针将会放在文件的末尾，所以写入的
#内容会新增到文件夹中，注意如果文件不存在，会自动创建一个新文件
#增加b，表示以二进制格式进行操作文件读写，如果文件是二进制文件，则选择此项如图片，视频，音频
#追加“+” 代表以读写模式打开文件
#w+ 会以部分覆盖的形式，可读写
#r+,可读写，其他与r相同
#下面为文件的定位
f=open("a.txt","r)
#seek(offset,whence) offset是偏移量，whence是位置，即相对于那个位置的偏移量  ，
#where有三个取值0,1,2分别表示开始位置，当前位置，和结尾位置，where默认为0      
f.seek(2)
#tell()可以告诉当前指针所在位置       
print(f.tell())  
#f.read(字节数)字节数默认为文件长度。下标会自动后移
#f.readline(limit)#读取一行的数据，指针自动到下一行，limit为限制的最大字节数，因为有的文件一行就有好多内容
#f.readlines()会自动的将文件按换行符进行处理，将处理好的每一行组成一个列表返回
# for in 可以直接遍历f本身，也可以遍历行列表
#f.readable() 返回TRUE OR FALSE判断当前文件是否可读，以免报错影响后续的程序的运行
import os
os.rename("b.txt","bb.txt")#修改文件名称
os.rename("first","one")#它也可以修改目录名称，但是只能修改单级目录或文件
os.renames("one/one.txt","two/two.txt")#os.renames是按照树状结构去逐层修改的，可以修改多级目录和文件       
os.remove("filepath")#删除文件，如果文件不存在就会报错
os.rmdir("目录”)#只能删除空目录
os.removedirs()#会递归的删除整个路径上的文件         
os.mkdir("文件夹名称")#不支持多级目录的创建，只能创建一级目录，如果文件已存在，再创建就会报错 
os.getcwd()#获取当前目录
os.chdir("目标目录”)#改变默认目录
os.listdir("./")#获取目录内容列表  ./指的是当前Python目录，列举的是一级目录，../列举的是上一级目录
#文件复制，注意前后编码一致，写入时最好是追加模式a
#按照文件后缀名，划分到不同的文件夹
import shutil
shutil.move()#shutil是一个高级的文件操作包 
#os.path.dirname可以把一个path中最后一个名字去掉
print(os.path.dirname("E:/Read_File/read_yaml.py"))
#结果：
E:/Read_File

