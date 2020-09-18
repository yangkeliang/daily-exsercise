import requests
import dbtools as db
import pandas as pd
data = pd.read_excel("data.xlsx","接口")

# url = data["url"][0]#获取轮播图接口测试
# res = requests.get(url)
# assert res.status_code == 200
# assert res.json()["status"] == 200
# for i in res.json()["data"]:
#     sql = "select * from t_title_img where id = {}".format(i["id"])
#     assert(len(db.query(sql)) != 0 )
# data["result"][0] = "获取轮播图接口成功！"
# data.to_excel("data.xlsx","接口")

url = data["url"][1]#登录接口测试
head = eval(data["head"][1])

data1 = eval(data["data"][1])
res = requests.post(url = url,headers = head,json = data1)
assert res.status_code == 200
assert res.json()["status"] == 200
sql = "select * from t_user where username = '{}';".format(data1["username"])
res1 = db.query(sql)
assert len(res1) != 0
data["result"][1] = "登录接口成功！"
data.to_excel("data.xlsx","接口")
token = res.json()["data"]["token"]

url1 = data["url"][2]#登录发表灵感测试
head1 = eval(data["head"][2])
head1["token"] = token
data2 = eval(data["data"][2])
res2 = requests.post(url = url1,headers = head1,json = data2)
assert res2.status_code == 200
assert res2.json()["status"] == 200
data["result"][2] = "登录发表灵感接口成功！"
data.to_excel("data.xlsx","接口")


