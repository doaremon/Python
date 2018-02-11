#功能
def show_meun():
    print("*" * 50)
    print("欢迎使用【名片管理系统v1.0】")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

#输入查询名片
def select_cards(card_list,name):
    for indexname in card_list:
        print(indexname)
        if(indexname==name):
            print("当前系统找到%s这张名片" % name)
            break
    else:
        print("找不到%s人"%name)

#显示全部数据
def show_allcards(card_list):
    mylen=len(card_list)
    if mylen==0:
        print("暂无数据")
    for name in card_list:
        print("当前名片:%s"%name)

#添加名片数据
def add_cards(card_list,name):
    card_list.append(name)
