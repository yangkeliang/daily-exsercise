import requests
def get_reponse(url):
    try:
        kv={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"

if (__name__=="__main__"):
    url=input("请输入url：")
    print(get_reponse(url))