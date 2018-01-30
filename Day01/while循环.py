import random
#while循环
i=1
# while (i<=3):
#     print("hello python")
#赋值运算符
a=10
c=20
a+=c
print("a=%d"%a)

randindex=random.randint(1,100)
print("randindex产生的随机数:randindex=%d"%randindex)
#循环计算
#需求，计算0-100之间累加求和
all=0
myindex=0
while(myindex<=100):
    all+=myindex
    myindex+=1
print("循环完成，结果是=%d"%all)
#需求，计算0-100中，所以偶数求和
index1=0
index=0
while(index<=100):
    if (index%2==0):
        index1+=index
    index+=1
print("偶数求和=%d" %index1)