#超市买苹果 定义苹果的单价
price=8.5
#要买多少斤
num=19
#价钱
money=price*num-5

#增强版
#输入苹果单价
apple_price=input("请输入苹果单价")
#输入数量
apple_num=input("请输入要买多少")
#目前两个都是str类型，需要转int才可以*
apple_price=float(apple_price)
apple_num=float(apple_num)

apple_money=apple_price*apple_num
print(apple_money)
print("程浩")
