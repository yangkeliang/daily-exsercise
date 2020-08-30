import re
import requests
def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("返回异常")
def gettext(txt):
    r=re.findall(r"ent\">[\s\S]+?</div>",txt)
    r[0]=r[0].replace("<br><br>","")
    r[0]=r[0].replace("ent\">","")
    r[0]=r[0].replace("iv>","")
    return r[0]
  
def filltext(txt,i):
    with open("小说.txt","a",encoding="utf-8") as f:
        f.write("第"+str(i+1)+"章"+"\n")
        f.write(txt+"\n")
        f.write("-----------------------------------------------------------------------------"+"\n")

def main(url,i):
    filltext(gettext(gethtml(url)),i)


if __name__=="__main__":
    i=int(input("请输入章数："))
    for i in range(i):
        url="https://www.book900.com/9_9325/"+str(i)
        main(url,i)