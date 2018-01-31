#元组
a=list("abcdef")
my_tuple=(1,2,3,4,5,"程浩",1.23,"程浩")
#print(my_tuple[0])
a[0]="2"
#print(my_tuple[0])
#取出索引
print(my_tuple.index("程浩"))
#统计元组中的个数
print(my_tuple.count("程浩"))

#元组和列表进行转换
myarray=[1,2,3,4,5]

print(type(myarray))
print(type(my_tuple))

print("开始转换")

print(type(tuple(myarray)))
print(type(list(my_tuple)))