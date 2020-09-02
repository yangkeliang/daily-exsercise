class List_of_ykl:
    def __init__(self,mylist):
        self.mylist=mylist
    def maopao(self):#冒泡算法
        length=len(self.mylist)
        for j in range(length-1):
            for i in range(length-1):
                if self.mylist[i]>self.mylist[i+1]:
                    t=self.mylist[i]
                    self.mylist[i]=self.mylist[i+1]
                    self.mylist[i+1]=t
        return self.mylist
    def xuanze(self):#选择算法
        length=len(self.mylist)
        for i in range(length):
            for j in range(i+1,length):
                if self.mylist[i] > self.mylist[j]:
                    t=self.mylist[i]
                    self.mylist[i]=self.mylist[j]
                    self.mylist[j]=t
        return self.mylist

if __name__=="__main__":
    ykl=List_of_ykl([1,8,4,2,57,2,673,36,90,6,32,2])
    print("冒泡算法排序：{}".format(ykl.maopao()))
    print("选择算法排序：{}".format(ykl.xuanze()))

          

