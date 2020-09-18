import requests
from bs4 import BeautifulSoup

def get_soup(url):
    '''获取美丽汤'''
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,"html.parser")
        return soup
    except:
        print("存在异常")

def fill_que(soup):
    '''存储题目'''
    info_li=[]
    info_li.append(soup("strong")[0].next_sibling)
    with open("题目.txt","a",encoding="utf-8") as f:
        for j in info_li:
            f.write(j+"\n")
        f.write("---------------------------------"+"\n")

if __name__=="__main__":
    for i in range(4,101):
        url="https://www.runoob.com/python/python-exercise-example"+str(i)+".html"
        soup=get_soup(url)
        fill_que(soup)
