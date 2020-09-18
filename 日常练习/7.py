def counteven(n):
    count = 0
    for i in range(n+1):
        if i % 2 ==0:
            count=count+1
    return count

def yinshu(n):
    list1=[]
    for i in range(1,n+1):
        if n % i ==0:
            list1.append(i)
    return list1

def getdic(dic):
    list1=[]
    for i in dic.values():
        if "可亮" in i:
            list1.append(i)
    return list1

if __name__=="__main__":
    print(counteven(1000))
    print(yinshu(235))
    print(getdic({"aa":"1可亮","va":"2可亮","ca":"3可亮","da":"1看看","oa":"1此处"}))

