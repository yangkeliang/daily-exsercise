def getkey():
    list1=[]
    while True:
        a=input("请输入键：")
        if a == "" :
            break
        list1.append(a)
    return list1 

def getvalue(list0):
    i=len(list0)
    list1=[]
    for k in range(i):
        a=input("请输入值：")
        list1.append(a)
    return list1 

def makedic(list1,list2):
    dic={}
    for i,j in zip(list1,list2):
        dic[i]=j
    return dic

def showdit(a):
    print(a)

if __name__ == "__main__":
    a=getkey()
    b=getvalue(a)
    c=makedic(a,b)
    showdit(c)



    
    