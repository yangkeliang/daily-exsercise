class Light:
    def __init__(self,time,name):
        self.time=time
        self.name=name
    def showtime(self):
        while self.time>0:
            print("{0}灯还有{1}秒".format(self.name,self.time))
            self.time=self.time-1

if __name__=="__main__":
    redlight=Light(35,"红")
    greenlight=Light(20,"绿")
    yellowlight=Light(5,"黄")
    redlight.showtime()
    greenlight.showtime()
    yellowlight.showtime()
