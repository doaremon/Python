class Zoology:
    def eat(self):
        print("吃---")
    def run(self):
        print("跑--")
class Dog(Zoology):
    def jiao(self):
        print("汪汪汪--")
class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞--哈哈")
    def eat(self):
        super().eat()
        print("我是哮天犬，我吃肉---")

xiaotianquan=XiaoTianQuan()
xiaotianquan.fly()
xiaotianquan.jiao()
xiaotianquan.run()
xiaotianquan.eat()