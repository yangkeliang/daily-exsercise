def regist():#注册
    user_dic={}
    name=input("请输入姓名：")
    passwd=input("请输入密码：")
    user_dic[name]=passwd
    return user_dic

def scr_regist():#屏幕交互注册
    user_dic={}
    while True:
        ans=input("开始注册？y or n:")
        if ans=="y":
            usr_info=regist()
            if list(usr_info.keys())[0] in list(user_dic.keys()):#判断是否重复注册
                print("改用户已注册，请重新输入：")
            else:
                user_dic.update(usr_info)#更新字典
        elif ans=="n":
            break
        else:
            print("输入错误，请输入y或n：")
    return user_dic

def login(user_dic):#用户登录
    print("只有5次登录机会")
    for i in range(5,0,-1):
        name=input("请输入姓名：")
        passwd=input("请输入密码：")
        if user_dic.get(name)==passwd:
            print("登录成功!")
            break
        elif user_dic.get(name)==None:
            print("无此账号,剩余{}次机会".format(i-1))
        else:
            print("密码错误,剩余{}次机会".format(i-1))

def scr_login(user_dic):#屏幕交互登录
    while True:
        ans=input("是否登录？y or n:")
        if ans=="y":
            login(user_dic)
        elif ans=="n":
            break
        else:
            print("输入错误，请输入y或n：")

if __name__=="__main__":
    user_dic=scr_regist()
    scr_login(user_dic)
    


    
