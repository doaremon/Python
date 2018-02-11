#公共函数
#max min 函数，查找最大值和最小值
t_list=[2,3,5,8,1,4,10]
print("当前最大值为%d"%max(t_list))
print("当前最小值为%d"%min(t_list))
#也就是在字典中，只会比较key不会比较值
t_dict={"a":"z","b":"y","c":"x"}
print(max(t_dict))
print(min(t_dict))
#cmp 函数 3.0以上的删除了cmp的函数   字典不能比较大小   元组，列表都可以用这个比较大小

#len函数 计算容器中元素的个数
print("t_list中含有的个数：%d 个"%len(t_list))

#del删除变量
#del(t_list)
#print(t_list)#删除变量

#切片  列表和元组都可以切片，字典不可以切片，因为字典都是key和value
print(t_list[0:4])
#运算符 *  列表和元组可以使用，字典不可以使用
print([1,2]*2)
print((1,2,3)*3)
#+ 运算符
print([1,2,3]+[4,5,6])
print("hello "+"python")
print((1,2,3,4)+(5,6,7,8))
# in   指定元素是否包含在列表，字典（判断key），元组
# not in
print("a" in ("a","b","c"))
print("10" in "123456")

#完整的for循环用法
# for 变量 in 集合:
#     循环体代码
# else:
#     没有通过break退出循环，循环结束后，会执行的代码
#break 直接不执行else
for index in [1,2,3,4,5]:
    print(index)
    if (index==2):
        break
else:
    print("循环结束")