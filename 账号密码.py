def regist():#注册
    user_dic={}
    name=input("请输入姓名：")
    passwd=input("请输入密码：")
    user_dic[name]=passwd
    return user_dic

def scr_info():#屏幕交互
    user_dic={}
    while True:
        ans=input("开始注册？y or n:")
        if ans=="y":
            user_dic.update(regist())#更新字典
        elif ans=="n":
            break
        else:
            print("输入错误，请输入y或n：")
    return user_dic

def login(user_dic):#用户登录
    print("只有5次登录机会")
    for i in range(5,-1,-1):
        name=input("请输入姓名：")
        passwd=input("请输入密码：")
        if user_dic.get(name)==passwd:
            print("登录成功!")
            break
        elif user_dic.get(name)==None:
            print("无此账号,"+"剩余"+str(i-1)+"次机会")
        else:
            print("密码错误,"+"剩余"+str(i-1)+"次机会")

if __name__=="__main__":
    user_dic=scr_info()
    login(user_dic)
    
