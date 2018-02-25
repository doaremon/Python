#定义一个类
class Person:
    def name(self,name):
        #self 可以点出半路出来的变量
        print("我的名字是%s,年龄是%s"%(name,self.age))
    def run(self):
        print("我会跑")

#创建人对象
tom=Person()
#这种半路出来的不建议使用
tom.age="20"
tom.name("小胖")
tom.run()



class cat:
    #这个初始化方法和android 的oncreate方法一样，上来就执行方法
    def __init__(self):
        print("这是个初始化方法")
        #self.属性名=属性的初始值  也就是 在类中，定义初始化属性，都在__init__中定义
        self.name="Tom"

QQ=cat()
print(QQ.name)