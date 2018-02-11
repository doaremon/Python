import 名片管理系统.cards_utils
# 名片管理系统入口 程浩
card_list=[]
while True:
    名片管理系统.cards_utils.show_meun()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    if action_str in ["1","2","3"]:
        if action_str=="1":
            add_name=input("请输入要添加的名片名字")
            名片管理系统.cards_utils.add_cards(card_list,add_name)
        elif action_str=="2":
            名片管理系统.cards_utils.show_allcards(card_list)
        elif action_str=="3":
            card_name=input("请输入要查询的名片名字")
            名片管理系统.cards_utils.select_cards(card_list,card_name)
    elif action_str=="0":
        print("登出成功")
        #退出
        break
    else:
        print("您输入有误，请重新输入")