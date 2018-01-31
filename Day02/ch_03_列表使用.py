import keyword
print("关键字有%s"%keyword.kwlist)
#列表使用
name_list=["张三","李四","王五","赵六"]
#1，取值
print(name_list[2])
#2.去索引
index=name_list.index("李四")
print("这个在列表中的索引=%d"%index)
#3.修改
name_list[0]="哈哈"
print(name_list)
#4.增加数据 append方法，向列表追加数据
name_list.append("王小二")
print(name_list)
#insert指定位置
name_list.insert(2,"小妹妹")
print(name_list)
#extend 追加列表
index_list=["小龙女","悟空","沙僧"]
name_list.extend(index_list)
print(name_list)

#5.删除数据 3中方法  remove删除指定数据
name_list.remove("悟空")
print(name_list)
#pop不填参，删除最一个   或者填index
name_list.pop()
print(name_list)
#del也可以删除的   这个的本质是从内存中删除
del name_list[0]
print(name_list)
#clear 全删，清空数据
# name_list.clear()
# print(name_list)

#查看长度，
lens=len(name_list)
print("列表中现在的元素%d"%lens)
num=name_list.count("李四")
print("李四出现的次数%d"%num)

num_list=[1,5,2,9,10]
#sort 升序
num_list.sort()
print(num_list)
#降序 reverse=True
num_list.sort(reverse=True)
print(num_list)

#反转
num_list.reverse()
print(num_list)
print("开始迭代遍历")
#遍历数组
for index2 in name_list:
    print("我的名字叫%s"%index2)