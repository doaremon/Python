#格式化输出字符串
name="程浩"
age=28
print("我的名字叫%s,请多多关照。我今年%d岁。"%(name,age))
#这个08d 表示8位 如果前面没有，那么就补0
student_no=2
print("我的学号是%08d"%student_no)
#.2f 意思就是小数点后面显示2位，
price=8.5
num=7.5
money=price*num
print("苹果的单价是%.2f，需要购买的数量是%.2f。需要实际付款：%.2f" %(price,num,money))
#输出%    %%
inde=10
print("数据比例是%.2f%%" %inde)