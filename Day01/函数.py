#函数
def sum(index1,index2):
    """
    这个是函数哦
    :param index1:  index1
    :param index2:   index2
    :return:  返回值
    """
    con=index1+index2
    print("%d +%d=%d"%(index1,index2,con))
    return con

s=sum(4,2)
print("函数返回值%d"%s)