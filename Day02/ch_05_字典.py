#字典
#字典输出的顺序是无序的，随机出来的。
chenghao={"name":"程浩",
          "age":28,
          "sex":"男",
          "height":171}
print(chenghao)
#1,取值  key必须存在，否则报错
myname=chenghao["name"]
print(myname)
#2，增加。修改
chenghao["name"]="小妹妹"
chenghao["school"]="科技大学"
print(chenghao)
#3，删除 pop(key)  key必须存在，否则报错
chenghao.pop("name")
print(chenghao)

ch={"name":"程浩",
          "age":28,
          "sex":"男",
          "height":171}
#4.统计键值对数量
print(len(ch))
#5，合并字典  update 这个会覆盖
temp_dict={"QQ":"375130788"}
ch.update(temp_dict)
print(ch)
#6，清空字典
ch.clear()
print(ch)

xiaoxiao={"name":"程浩",
          "sex":"男"
         }
#7.循环遍历字典
for key in xiaoxiao:
    print("key为%s，对应的key=%s"%(key,xiaoxiao[key]))

#列表中保存多个字典
car_list=[{"name":"张三",
           "qq":"12345",
           "phone":"9876543321"},
          {"name":"李四",
           "qq":"999999",
           "phone":"10086"},
          {"name":"王五",
           "qq":"66666",
           "phone":"10000"}]
for card_info in car_list:
    print(card_info)