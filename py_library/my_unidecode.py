import unidecode
#这个模块的作用：
就是能够讲一个text中所有非ASCII编码变成最接近的ASCII
I'm trying to remove all non-ascii characters from a text document. 
I found a package that should do just that, 
It should accept a string and convert all non-ascii characters to the closest ascii character available. 
#它接收一个string并将所有非ascii字符转换为最接近的ascii字符
#例子如下：
print(unidecode.unidecode("你好打发第三方"))
print(unidecode.unidecode("こんにちは皆、こんにちは。"))
print(unidecode.unidecode("Xin chào mọi người, xin chào."))
#返回的结果，反正就是把他们返回最接近他们的发音拉丁字母(ASC)
#Ni Hao Da Fa Di San Fang 
#konnichihaJie , konnichiha. 
#Xin chao moi nguoi, xin chao.
