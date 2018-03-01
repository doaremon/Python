#封装
# 需求
# 小明体重75.0公斤
# 小明每次跑步减肥0.5公斤
# 小明每次吃东西增加1公斤
class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return "我叫%s，我现在的体重有%.2f"%(self.name,self.weight)
    def run(self):
        self.weight-=0.5
        print("%s刚刚跑步后的体重：%0.2f"%(self.name,self.weight))
    def eat(self):
        self.weight+=1
        print("%s刚刚吃饭后的体重：%.2f" % (self.name,self.weight))

Xiaoming=Person("小明",86.0)
Xiaoming.run()
Xiaoming.eat()
print(Xiaoming)
Xiaomei=Person("小美",45.0)
Xiaomei.run()
Xiaomei.eat()
print(Xiaomei)