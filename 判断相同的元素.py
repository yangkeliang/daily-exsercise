class Mylist:
    def __init__(self,mylist):
        self.mylist=mylist
    def getsame(self):
        same_list=[]
        for i in range(len(self.mylist)):
            for j in range(i+1,len(self.mylist)):
                if self.mylist[i] == self.mylist[j]:
                    same_list.append(self.mylist[i])
        return same_list
        
if __name__=="__main__":
    mylist=Mylist([1,1,1,13,4,62,61,15,61,12,11,11,56,32,56])
    print(mylist.getsame())

