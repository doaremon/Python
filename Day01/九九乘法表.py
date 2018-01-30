#简单需求，打印小星星
i=1
while (i<=5):
    #print("i=%d" %i)
    print("*" *i)
    i+=1

print("==============================")
#九九乘法表
index=1
while (index<=9):
    print()
    index1 = 1
    while(index1<=index):
        num=index*index1
        print("%d*%d=%d"%(index1,index,num),end="\t")
        index1+=1
    index+=1
