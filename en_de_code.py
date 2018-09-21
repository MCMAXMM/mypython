#在所有字符集中，最知名的可能要数被称为ASCII的7位字符集了。
#它是美国标准信息交换代码（American Standard Code for Information Interchange）的缩写, 为美国英语通信所设计。
#它由128个字符组成，包括大小写字母、数字0-9、标点符号、非打印字符（换行符、制表符等4个）以及控制字符（退格、响铃等）组成。
#但是，由于他是针对英语设计的，当处理带有音调标号（形如汉语的拼音）的欧洲文字时就会出现问题。
#把汉语、日语和越南语的一些相似的字符结合起来，在不同的语言里，
#使不同的字符代表不同的字，这样只用2个字节就可以编码地球上几乎所有地区的文字。因此，创建了UNICODE编码。
#它通过增加一个高字节对ISO Latin-1字符集进行扩展，当这些高字节位为0时，低字节就是ISO Latin-1字符。
#事实证明，对可以用ASCII表示的字符使用UNICODE并不高效，因为UNICODE比ASCII占用大一倍的空间，
#而对ASCII来说高字节的0对他毫无用处。为了解决这个问题，就出现了一些中间格式的字符集，他们被称为通用转换格式，
#即UTF（Universal Transformation Format）。常见的UTF格式有：UTF-7, UTF-7.5, UTF-8,UTF-16, 以及 UTF-32。
#decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
#encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
#有时python3会报错：AttributeError: 'str' object has no attribute 'decode'
#因为python3里str默认为 unicode 了吧。只能编码 encode 不能解码 decode。
#1.为了处理英文字符，产生了ASCII码。 
#2.为了处理中文字符，产生了GB2312。 
#3.为了处理各国字符，产生了Unicode。 
#4.为了提高Unicode存储和传输性能，产生了UTF-8，它是Unicode的一种实现形式。**
