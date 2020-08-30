import re
import requests
def gethtml(url,data):
    try:
        kv={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,params=data,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text)
        # return r.text
    except:
        print("返回异常")

# def gettext(i):


def main(name,page):
    url="https://uland.taobao.com/sem/tbsearch?spm=a2e15.8261149.07626516003.1.1eb929b4dVw70P&refpid=mm_26632258_3504122_32538762&clk1=0072c683e588a484eed2dabaa190d805"
    data={
    "keyword":name,
    "page":page}
    gethtml(url,data)

if __name__=="__main__":
    main(input("请输入搜索商品名："),input("请输入页码："))