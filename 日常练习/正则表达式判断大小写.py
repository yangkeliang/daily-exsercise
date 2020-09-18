import re

def panduan(a):
    if re.match(r"[a-z]",a):
        print("小写")
    elif re.match(r"[A-Z]",a):
        print("大写")
    else:
        print("请输入大小写字母，谢谢！")

if(__name__=="__main__"):
    a=input("请输入大小写字母：")
    panduan(a)
