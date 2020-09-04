import easygui as eg

def gui_regist():#注册
    user_dic={}
    usr_info=eg.multpasswordbox(msg="请输入用户名密码",title="用户登录接口",fields=("用户名","密码"))
    name=usr_info[0]
    passwd=usr_info[1]
    user_dic[name]=passwd
    return user_dic

def gui_scr_regist():#屏幕交互注册
    user_dic={}
    while True:
        ans=eg.enterbox(msg="开始注册？y or n:",title="注册接口")
        if ans=="y":
            usr_info=gui_regist()
            if list(usr_info.keys())[0] in list(user_dic.keys()):#判断是否重复注册
                print("")
                eg.msgbox(msg="改用户已注册，请重新输入：",title="用户注册接口",ok_button="重新注册")
            else:
                user_dic.update(usr_info)#更新字典
        elif ans=="n":
            break
        else:
            eg.msgbox(msg="输入错误，请输入y或n：",title="用户注册接口",ok_button="重新注册")
    return user_dic

def gui_login(user_dic):#用户登录
    eg.msgbox(msg="只有5次登录机会",title="用户登录接口",ok_button="继续")
    for i in range(5,0,-1):
        ans=eg.multpasswordbox(msg="请输入用户名密码",title="用户登录接口",fields=("用户名","密码"))
        name=ans[0]
        passwd=ans[1]
        if user_dic.get(name)==passwd:
            eg.msgbox(msg="登录成功!",title="用户登录接口",ok_button="重新登录")
            break
        elif user_dic.get(name)==None:
            eg.msgbox(msg="无此账号,剩余{}次机会".format(i-1),title="用户登录接口",ok_button="重新登录")
        else:
            eg.msgbox(msg="密码错误,剩余{}次机会".format(i-1),title="用户登录接口",ok_button="重新登录")
            
def gui_scr_login(user_dic):#屏幕交互登录
    while True:
        ans=eg.enterbox(msg="是否登录？y or n:",title="登录接口")
        if ans=="y":
            gui_login(user_dic)
        elif ans=="n":
            break
        else:
            eg.msgbox(msg="输入错误，请输入y或n：",title="用户登录接口",ok_button="重新登录")

if __name__=="__main__":
    user_dic=gui_scr_regist()
    gui_scr_login(user_dic)
