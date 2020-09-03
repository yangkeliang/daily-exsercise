class Cal:
    def __init__(self,*para):
        self.para=para
    def jian(self):
        length=len(self.para)
        result=self.para[0]
        for i in range(1,length):
            result=result-self.para[i]
        return result
    def jia(self):
        length=len(self.para)
        result=self.para[0]
        for i in range(1,length):
            result=result+self.para[i]
        return result
    def chen(self):
        length=len(self.para)
        result=self.para[0]
        for i in range(1,length):
            result=result*self.para[i]
        return result
    def chu(self):
        length=len(self.para)
        result=self.para[0]
        for i in range(1,length):
            result=result/self.para[i]
        return result

if __name__=="__main__":
    cal=Cal(1,2,3,4,5,6)
    print(cal.jia())
    print(cal.jian())
    print(cal.chen())
    print(cal.chu())
