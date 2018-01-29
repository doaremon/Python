import random
#while循环
i=1
while (i<=3):
    print("hello python")
    i+=1
print("循环结束，当前i=%d"%i)

#赋值运算符
a=10
c=20
a+=c
print("a=%d"%a)

randindex=random.randint(1,100)
print("randindex产生的随机数:randindex=%d"%randindex)