import pymysql

def query(sql):
    # ip=input("请输入数据库IP地址：")
    # user_name=input("请输入用户名：")
    # password=input("请输入密码：")
    # database=input("请输入数据库名：")
    # ip="192.144.148.91"
    # user_name="ljtest"
    # password="Lj123456+"
    # database="ljtestdb"
    ip="192.144.148.91"
    user_name="ljtest"
    password="Lj123456+"
    database="ljtestdb"
    db=pymysql.connect(host=ip,user=user_name,passwd=password,db=database)#连接数据库
    cur=db.cursor()#创建游标
    cur.execute(sql)#查询
    result=cur.fetchall()#获取查询值
    db.close()
    return result

if __name__=="__main__":
    res=query("select * from t_user where username = '{}'".format("wwww"))
    # res=query("select * from t_goods where id = '{}'".format("iPhone"))
    print(res)
