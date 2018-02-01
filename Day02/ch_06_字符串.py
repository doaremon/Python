#字符串的学习
#1,字符串取单个值
ch="程浩andchenghao"
print(ch[4])
#2.字符串长度
hello_str="hello python llo"
print(len(hello_str))
#3.统计某个小字符串出现的次数
print(hello_str.count("llo"))
#4.去位置
print(hello_str.index("llo"))
#5.判断空白字符   空格 \t \n \r 都属于空白字符
space_str="  "
print(space_str.isspace())
#6.判断字符串是否只包含数字
#区别  这个三个方法都不能判断小数
#unicode 字符串
num_str="1"
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
#7.判断字符串开头
index_str="你好，我是Doraemon"
print(index_str.startswith("我你"))
#8.判断字符串结尾
print(index_str.endswith("我你"))
#9.查找指定字符串   find要比index的好。因为index如果没有会报错，而find不会报错
print(index_str.find("好"))
#10.替换字符串 replace不会修改原来的字符串
print(index_str.replace("我","My"))
#11.文本对其 一般都是调整歌词或是诗词的方法，这样比java要高级点
poem=["登鹳雀楼","王之涣","白日依山尽","黄河入海流","欲穷千里目","更上一层楼"]
for index in poem:
    print("|%s|"%index.center(10," "))
#12.rjust 和 ljust  右对齐和左对齐
#13.取出空白字符strip   和java trim一样
str1=" ni "
print(str1.strip())
#14.字符串的分割
str_split="今天是个好天气-哈哈-吼"
#str_list=str_split.split("-")
result="???".join(str_split)   #join 这个方法的意思，把str_split一个一个拆开，然后拼接？？？ 很☹️。没啥用啊
print(result)

#15.字符串的切片   从大字符串切 出小字符串   语法:    字符串[开始索引：结束索引：步长]
my_num="0123456789"
#字符串逆序
print(my_num[::-1])

