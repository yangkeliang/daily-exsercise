import requests
import time
def get_reponse(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if (__name__=="__main__"):
    url=input("请输入url：")
    time_start=time.time()
    for i in range(100):
        print(get_reponse(url))
    time_end=time.time()
    print(time_end-time_start)
