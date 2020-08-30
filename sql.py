import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="123456")
cur=con.cursor()
cur.execute("create database if not exists python default charset utf8")
cur.execute("use python")
cur.execute("create table if not exists py1 (id int(23),name varchar(233)) ")
i=1
for name in ["ykl","zzz","hhh","mlb","jgl","1994"]:
    cur.execute("insert into py1 (id,name) values (%d,'%s')"%(i,name))
    i=i+1
con.commit()