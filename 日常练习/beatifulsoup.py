from bs4 import BeautifulSoup
import requests
r=requests.get("https://python123.io/ws/demo.html")
soup=BeautifulSoup(r.text,"html.parser")
print(list(soup.body.descendants))