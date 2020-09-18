import requests
def get_reponse(keyword):
    try:
        kv={"wd",keyword}
        r=requests.get("http://www.baidu.com/s",params=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"



if (__name__=="__main__"):
    keyword=input("请输入搜索内容：")
    print(get_reponse(keyword))