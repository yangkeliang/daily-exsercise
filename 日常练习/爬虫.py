# import urllib.request
# response=urllib.request.urlopen("https://www.cnblogs.com/wjr2018/p/10223341.html")
# html=response.read()
# print(html)

# response=urllib.request.urlopen("https://pic.cnblogs.com/face/1525097/20181102103511.png")
# html=response.read()
# with open("kyl.png","wb") as f:
#     f.write(html)

import requests
response=requests.get("https://www.cnblogs.com/wjr2018/p/10223341.html")
print(response.text)
