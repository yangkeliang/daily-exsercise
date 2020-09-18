def panduan(list1,sum):
    a = 0
    for i in list1:
        list1.remove(i)
        for j in list1:
            list1.remove(j)
            for k in list1:
                list1.remove(k)
                if i+j+k == sum:
                    a = 1
                    return "True"
                    break
    if a == 0:
        return "False" 

if __name__ == "__main__":
    print(panduan([1,2,3,4,5,1,1,1,1,1,1,2],4))