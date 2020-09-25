import random
import time

# 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束

class Turtle:
    '''龟类'''
    def __init__(self):
        '''初始化体力值、初始坐标'''
        self.body = 100#体力
        self.x = random.randint(1,10)#x坐标
        self.y = random.randint(1,10)#y坐标

    def move(self):
        '''移动方法'''
        self.axis=random.choice([0,1])#移动坐标轴，0x轴，1y轴
        self.dir=random.choice([-1,1])#移动方向
        self.step=random.choice([1,2])#移动步长
        self.length=self.dir*self.step#移动结果
        #先移动，再判断x是否在边界内
        #移动
        if self.axis == 0:#x轴移动
            self.x=self.x+self.length
        else:#y轴移动
            self.y=self.y+self.length
        #判断是否在边界内
        if self.x <0:#不在边界之内，反弹
            self.x = self.step - (self.x - self.length )
        elif self.x >10:#不在边界之内，反弹
            self.x = 2*10 - self.step - (self.x - self.length )
        elif self.y <0:#不在边界之内，反弹
            self.y = self.step - (self.y - self.length )
        elif self.y >10:#不在边界之内，反弹
            self.y = 2*10 - self.step - (self.y - self.length )
        else:#在边界内啥也不做
            pass
        self.body = self.body -1#移动一步后，体力减1

    def bodychange(self):
        '''体力消耗'''
        self.body = self.body -1

    def eat(self):
        '''吃鱼方法'''
        self.body = self.body +20#体力增加20

class Fish:
    '''鱼类'''
    def __init__(self):
        '''初始化，鱼没有体力'''
        self.x = random.randint(1,10)#x坐标
        self.y = random.randint(1,10)#y坐标

    def move(self):
        '''移动方法'''
        self.axis=random.choice([0,1])#移动坐标轴，0x轴，1y轴
        self.dir=random.choice([-1,1])#移动方向
        self.step=1#移动步长
        self.length=self.dir*self.step#移动结果
        #先移动，再判断x是否在边界内
        #移动
        if self.axis == 0:#x轴移动
            self.x=self.x+self.length
        else:#y轴移动
            self.y=self.y+self.length
        #判断是否在边界内
        if self.x <0:#不在边界之内，反弹
            self.x = self.step - (self.x - self.length )
        elif self.x >10:#不在边界之内，反弹
            self.x = 2*10 - self.step - (self.x - self.length )
        elif self.y <0:#不在边界之内，反弹
            self.y = self.step - (self.y - self.length )
        elif self.y >10:#不在边界之内，反弹
            self.y = 2*10 - self.step - (self.y - self.length )
        else:#在边界内啥也不做
            pass

if __name__=="__main__":
    turtle = Turtle()
    fish_list = []
    for i in range(10):
        fish = Fish()
        fish_list.append(fish)
    while(turtle.body != 0 and len(fish_list) != 0):#乌龟体力未消耗完及鱼儿数量不等于0时执行循环
        print("乌龟坐标：({}，{})，乌龟体力：{}".format(turtle.x,turtle.y,turtle.body))
        for i in fish_list:
            print("鱼{}坐标：({}，{})".format(fish_list.index(i),i.x,i.y),end =" ")
        print("\n")
        turtle.move()#乌龟移动
        for i in fish_list:#鱼移动
            i.move()
            if turtle.x == i.x and turtle.y == i.y:#判断是否能吃到，坐标是否重合
                turtle.body = turtle.body + 20
                fish_list.remove(i)
            else:
                pass
        # time.sleep(1)
    print("游戏结束")