import pymysql as psql
import easygui as eg

def connect(sql):
    # host=eg.enterbox(msg="请输入ip地址",title="sql接口")
    # user=eg.enterbox(msg="请输入用户名",title="sql接口")
    # passwd=eg.enterbox(msg="请输入密码",title="sql接口")
    # db=eg.enterbox(msg="请输入数据库",title="sql接口")
    host="localhost"
    user="root"
    passwd="123456"
    db="test23"
    con=psql.connect(host=host,user=user,passwd=passwd,db=db)
    cur=con.cursor()
    cur.execute(sql)
    res=cur.fetchall()
    con.commit()
    return res

def Regist():
    while True:
        name=eg.enterbox(msg="请输入用户名",title="注册接口")
        passwd=eg.enterbox(msg="请输入密码",title="注册接口")
        length=len(connect("select * from t_userinfo where name ='{}'".format(name)))
        if length != 0:
            eg.msgbox(msg="账号名存在，请重新登录！",title="提示信息",ok_button="重新注册")
        else:
            sql="INSERT INTO t_userinfo (name,passwd) VALUES ('{}', '{}')".format(name,passwd)
            break
    return sql

if __name__=="__main__":
    try:
        connect(Regist())   
    except Exception as a:
        print("问题是：{}".format(a))