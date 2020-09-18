dic={}
while True:
    a=input("请输入账号：")
    b=input("请输入密码：")
    if a=="end" and b=="end":
        break
    elif len(a)>=5 and len(a)<=18 and len(b)>=6 and len(b)<=12 and ord(a[0])>=97 and ord(a[0])<=122:
        dic[a]=b
    else:
        print("do again") 
print(dic)
