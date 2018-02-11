# 列表中加字典的功能
list_person=[]
name=input("请输入姓名")
phone=input("请输入电话")
age=input("请输入年龄")
my={}
my["name"]=name
my["phone"]=phone
my["age"]=age
list_person.append(my)
print(list_person)