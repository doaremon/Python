#封装
# 摆放家具案例
# 需求
# 1，房子有户型，总面积，家具名称
# 2.家具有名字和占地面积，其中，席梦思bed 占地面4 衣柜chest占地面积2 餐桌table占地面积1.5
# 3.将上面三个家具添加到房子中
# 4.打印房子，要求输出：户型,总面积，剩余面积，家具名称列表

class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return "新增家具%s ，这个家具占地面积 %.2f"%(self.name,self.area)
class House:
    def __init__(self,house_type,area,free_area,item_list):
        self.house_type=house_type
        self.area = area
        self.free_area = free_area
        self.item_list = item_list
    def __str__(self):
        for index in self.item_list:
            self.free_area-=index.area
        return "房屋户型%s," \
               "总面积%.2f," \
               "房屋剩余面积%.2f"%(self.house_type,self.area,self.free_area)
    def add(self,myhouseitem):
        self.item_list.append(myhouseitem)
bed=HouseItem("席梦思",4)
chest=HouseItem("衣柜",2)
table=HouseItem("餐桌",1.5)
print(bed)
print(chest)
print(table)
print("家具已经买好")
myhouse=House("大三居",100,100,[])
myhouse.add(bed)
myhouse.add(chest)
myhouse.add(table)

print(myhouse)