#在前面加__就是私有的
class Women:
    def __init__(self,name):
        self.name=name
        self.__age=19
    def secret(self):
        print("%s的年龄是%d"%(self.name,self.__age))

xiaomei=Women("小美")
print("姓名：%s"%xiaomei.name)
print("年龄%d"%xiaomei._Women__age)